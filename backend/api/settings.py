from __future__ import annotations

import os
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path


def _split_csv(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


@dataclass(frozen=True)
class ApiSettings:
    cors_origins: list[str]
    dify_base_url: str
    dify_api_key: str
    dify_default_user: str
    dify_timeout_seconds: float
    dify_max_upload_bytes: int
    dify_llm_provider: str
    dify_llm_model: str
    dify_embedding_provider: str
    dify_embedding_model: str
    dify_markdown_dir: Path

    @classmethod
    def from_env(cls) -> ApiSettings:
        return cls(
            cors_origins=_split_csv(
                os.getenv(
                    "API_CORS_ORIGINS",
                    "http://localhost:5173,http://127.0.0.1:5173",
                )
            ),
            dify_base_url=os.getenv("DIFY_BASE_URL", "http://localhost:80").rstrip("/"),
            dify_api_key=os.getenv("DIFY_API_KEY", ""),
            dify_default_user=os.getenv("DIFY_DEFAULT_USER", "skyrim-copilot-local"),
            dify_timeout_seconds=float(os.getenv("DIFY_TIMEOUT_SECONDS", "60")),
            dify_max_upload_bytes=int(os.getenv("DIFY_MAX_UPLOAD_BYTES", "10485760")),
            dify_llm_provider=os.getenv("DIFY_LLM_PROVIDER", "ollama"),
            dify_llm_model=os.getenv("DIFY_LLM_MODEL", "qwen3:14b"),
            dify_embedding_provider=os.getenv("DIFY_EMBEDDING_PROVIDER", "ollama"),
            dify_embedding_model=os.getenv("DIFY_EMBEDDING_MODEL", "bge-m3"),
            dify_markdown_dir=Path(
                os.getenv("UESP_PROCESSED_DIR", "data/processed/dify_markdown")
            ),
        )

    @property
    def dify_configured(self) -> bool:
        return bool(self.dify_base_url and self.dify_api_key)


@lru_cache(maxsize=1)
def get_settings() -> ApiSettings:
    return ApiSettings.from_env()
