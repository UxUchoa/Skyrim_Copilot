from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.routes import chat, files
from backend.api.schemas import HealthResponse
from backend.api.settings import get_settings


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
        title="Skyrim Copilot API",
        version="0.1.0",
        description=(
            "Local FastAPI proxy for the Skyrim Copilot frontend. The frontend "
            "must call this API only; Dify credentials stay in the backend .env."
        ),
        openapi_tags=[
            {
                "name": "chat",
                "description": "Streaming chat endpoint backed by the Dify app.",
            },
            {
                "name": "files",
                "description": "Image upload endpoint that returns Dify file ids.",
            },
            {
                "name": "health",
                "description": "Runtime configuration and readiness checks.",
            },
        ],
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "OPTIONS"],
        allow_headers=["*"],
    )

    app.include_router(files.router, prefix="/api")
    app.include_router(chat.router, prefix="/api")

    @app.get(
        "/api/health",
        response_model=HealthResponse,
        tags=["health"],
        summary="Check backend and Dify configuration",
        description=(
            "Returns local backend status and the Dify/Ollama settings loaded "
            "from the backend environment."
        ),
    )
    async def health() -> HealthResponse:
        current_settings = get_settings()
        return HealthResponse(
            status="ok",
            dify_configured=current_settings.dify_configured,
            dify_base_url=current_settings.dify_base_url,
            dify_llm_provider=current_settings.dify_llm_provider,
            dify_llm_model=current_settings.dify_llm_model,
            dify_embedding_provider=current_settings.dify_embedding_provider,
            dify_embedding_model=current_settings.dify_embedding_model,
            dify_markdown_dir=str(current_settings.dify_markdown_dir),
            dify_markdown_dir_exists=current_settings.dify_markdown_dir.exists(),
        )

    return app


app = create_app()
