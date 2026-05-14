from __future__ import annotations

from pydantic import BaseModel, Field


class UploadedFileResponse(BaseModel):
    upload_file_id: str
    name: str | None = None
    size: int | None = None
    mime_type: str | None = None


class ChatFile(BaseModel):
    upload_file_id: str
    type: str = "image"
    transfer_method: str = "local_file"

    def to_dify_payload(self) -> dict[str, str]:
        return {
            "type": self.type,
            "transfer_method": self.transfer_method,
            "upload_file_id": self.upload_file_id,
        }


class ChatStreamRequest(BaseModel):
    query: str = Field(min_length=1)
    conversation_id: str | None = None
    user: str | None = None
    files: list[ChatFile] = Field(default_factory=list)


class HealthResponse(BaseModel):
    status: str
    dify_configured: bool
    dify_base_url: str
    dify_llm_provider: str
    dify_llm_model: str
    dify_embedding_provider: str
    dify_embedding_model: str
    dify_markdown_dir: str
    dify_markdown_dir_exists: bool
