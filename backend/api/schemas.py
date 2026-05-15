from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class UploadedFileResponse(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "upload_file_id": "file-abc123",
                    "name": "skyrim-screenshot.png",
                    "size": 12345,
                    "mime_type": "image/png",
                }
            ]
        }
    )

    upload_file_id: str = Field(
        description="Dify upload file id to send later in chat files[]."
    )
    name: str | None = Field(default=None, description="Original uploaded filename.")
    size: int | None = Field(default=None, description="Uploaded file size in bytes.")
    mime_type: str | None = Field(default=None, description="Uploaded file MIME type.")


class ChatFile(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "upload_file_id": "file-abc123",
                    "type": "image",
                    "transfer_method": "local_file",
                }
            ]
        }
    )

    upload_file_id: str = Field(
        description="File id returned by POST /api/files/upload."
    )
    type: str = Field(default="image", description="Dify file type. Use image.")
    transfer_method: str = Field(
        default="local_file",
        description="Dify transfer method for uploaded local files.",
    )

    def to_dify_payload(self) -> dict[str, str]:
        return {
            "type": self.type,
            "transfer_method": self.transfer_method,
            "upload_file_id": self.upload_file_id,
        }


class ChatStreamRequest(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "query": "Quem sao os Greybeards em Skyrim?",
                    "conversation_id": None,
                    "user": "lucas",
                    "files": [],
                },
                {
                    "query": "E qual o papel deles na historia principal?",
                    "conversation_id": "4b624ea4-f786-4d9e-baa3-44a214d22c44",
                    "user": "lucas",
                    "files": [],
                },
                {
                    "query": "Analise esta imagem no contexto de Skyrim.",
                    "conversation_id": None,
                    "user": "lucas",
                    "files": [
                        {
                            "upload_file_id": "file-abc123",
                            "type": "image",
                            "transfer_method": "local_file",
                        }
                    ],
                },
            ]
        }
    )

    query: str = Field(
        min_length=1,
        description="User message to send to the Skyrim Copilot Dify app.",
        examples=["Quem sao os Greybeards em Skyrim?"],
    )
    conversation_id: str | None = Field(
        default=None,
        description=(
            "Use null for the first message. Reuse the conversation_id returned "
            "by the stream on the next messages."
        ),
    )
    user: str | None = Field(
        default=None,
        description="Optional user id sent to Dify. Defaults to DIFY_DEFAULT_USER.",
        examples=["lucas"],
    )
    files: list[ChatFile] = Field(default_factory=list)


class HealthResponse(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "status": "ok",
                    "dify_configured": True,
                    "dify_base_url": "http://localhost:80",
                    "dify_llm_provider": "ollama",
                    "dify_llm_model": "qwen3:8b",
                    "dify_embedding_provider": "ollama",
                    "dify_embedding_model": "bge-m3",
                    "dify_markdown_dir": "data/processed/dify_markdown",
                    "dify_markdown_dir_exists": True,
                }
            ]
        }
    )

    status: str
    dify_configured: bool
    dify_base_url: str
    dify_llm_provider: str
    dify_llm_model: str
    dify_embedding_provider: str
    dify_embedding_model: str
    dify_markdown_dir: str
    dify_markdown_dir_exists: bool
