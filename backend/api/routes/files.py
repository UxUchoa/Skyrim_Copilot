from __future__ import annotations

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile, status

from backend.api.dify_client import DifyAPIError, DifyClient, DifyConfigurationError
from backend.api.schemas import UploadedFileResponse
from backend.api.settings import ApiSettings, get_settings

router = APIRouter(tags=["files"])


@router.post(
    "/files/upload",
    response_model=UploadedFileResponse,
    summary="Upload an image to Dify",
    description=(
        "Uploads an image using multipart/form-data and returns a Dify file id. "
        "Send the returned `upload_file_id` in `files[]` when calling "
        "`POST /api/chat/stream`."
    ),
    responses={
        413: {"description": "Uploaded file exceeds DIFY_MAX_UPLOAD_BYTES."},
        415: {"description": "Only image/* uploads are supported."},
        502: {"description": "Dify returned an error while uploading the file."},
        503: {"description": "DIFY_API_KEY is missing or Dify is not configured."},
    },
)
async def upload_file(
    file: UploadFile = File(
        ...,
        description="Image file to upload. Supported MIME types start with image/.",
    ),
    user: str | None = Form(
        default=None,
        description="Optional user id sent to Dify. Defaults to DIFY_DEFAULT_USER.",
    ),
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
