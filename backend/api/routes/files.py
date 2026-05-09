from __future__ import annotations

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile, status

from backend.api.dify_client import DifyAPIError, DifyClient, DifyConfigurationError
from backend.api.schemas import UploadedFileResponse
from backend.api.settings import ApiSettings, get_settings

router = APIRouter(tags=["files"])


@router.post("/files/upload", response_model=UploadedFileResponse)
async def upload_file(
    file: UploadFile = File(...),
    user: str | None = Form(default=None),
    settings: ApiSettings = Depends(get_settings),
) -> UploadedFileResponse:
    mime_type = file.content_type or "application/octet-stream"
    if not mime_type.startswith("image/"):
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail="Only image uploads are supported.",
        )

    content = await file.read()
    if len(content) > settings.dify_max_upload_bytes:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail="Uploaded file exceeds DIFY_MAX_UPLOAD_BYTES.",
        )

    try:
        client = DifyClient(settings)
        uploaded = await client.upload_file(
            filename=file.filename or "upload",
            content=content,
            mime_type=mime_type,
            user=user or settings.dify_default_user,
        )
    except DifyConfigurationError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=str(exc),
        ) from exc
    except DifyAPIError as exc:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=str(exc),
        ) from exc

    return UploadedFileResponse(
        upload_file_id=uploaded.upload_file_id,
        name=uploaded.name,
        size=uploaded.size,
        mime_type=uploaded.mime_type or mime_type,
    )
