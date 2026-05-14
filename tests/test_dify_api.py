from __future__ import annotations

import json

import pytest

from backend.api.dify_client import (
    DifyAPIError,
    build_chat_payload,
    parse_dify_sse_line,
)
from backend.api.routes.chat import encode_sse
from backend.api.schemas import ChatFile


def test_build_chat_payload_uses_streaming_and_local_files() -> None:
    payload = build_chat_payload(
        query="Where is Bleak Falls Barrow?",
        conversation_id="conv-123",
        user="player-1",
        files=[ChatFile(upload_file_id="file-123")],
    )

    assert payload == {
        "inputs": {},
        "query": "Where is Bleak Falls Barrow?",
        "response_mode": "streaming",
        "conversation_id": "conv-123",
        "user": "player-1",
        "files": [
            {
                "type": "image",
                "transfer_method": "local_file",
                "upload_file_id": "file-123",
            }
        ],
    }


def test_build_chat_payload_sends_empty_conversation_for_new_chat() -> None:
    payload = build_chat_payload(
        query="Start a new chat.",
        conversation_id=None,
        user="player-1",
        files=[],
    )

    assert payload["conversation_id"] == ""
    assert payload["files"] == []


def test_parse_dify_sse_line_returns_json_payload() -> None:
    event = parse_dify_sse_line(
        'data: {"event":"agent_message","answer":"Hello","conversation_id":"conv-1"}'
    )

    assert event == {
        "event": "agent_message",
        "answer": "Hello",
        "conversation_id": "conv-1",
    }


def test_parse_dify_sse_line_ignores_non_data_and_done_lines() -> None:
    assert parse_dify_sse_line("event: ping") is None
    assert parse_dify_sse_line("data: [DONE]") is None


def test_parse_dify_sse_line_rejects_invalid_json() -> None:
    with pytest.raises(DifyAPIError):
        parse_dify_sse_line("data: {not-json}")


def test_encode_sse_formats_named_events() -> None:
    raw = encode_sse("conversation_id", {"conversation_id": "conv-1"})
    event_name, data, first_blank, trailing_blank = raw.split("\n")

    assert event_name == "event: conversation_id"
    assert json.loads(data.removeprefix("data: ")) == {"conversation_id": "conv-1"}
    assert first_blank == ""
    assert trailing_blank == ""
