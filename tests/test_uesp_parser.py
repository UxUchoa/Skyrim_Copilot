from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

from backend.ingest.uesp_parser import UespParser


FIXTURE_PATH = Path(__file__).parent / "fixtures" / "uesp_sample.html"


def test_parser_extracts_main_content_and_removes_noise() -> None:
    html = FIXTURE_PATH.read_text(encoding="utf-8")
    document = UespParser().parse(
        html,
        source_url="https://en.uesp.net/wiki/Skyrim:Bleak_Falls_Barrow",
        retrieved_at=datetime(2024, 1, 1, tzinfo=UTC),
    )

    rendered_sections = "\n\n".join(section.markdown for section in document.sections)
    headings = [section.heading for section in document.sections]

    assert document.title == "Bleak Falls Barrow"
    assert document.entity_type == "location"
    assert document.namespace == "Skyrim"
    assert "Skyrim-Places" in document.tags
    assert "Walkthrough" in headings
    assert "Bleak Falls Barrow is an ancient Nordic tomb" in rendered_sections
    assert "Dragonstone" in rendered_sections
    assert "Navigation noise" not in rendered_sections
    assert "Table of contents noise" not in rendered_sections
    assert "[edit]" not in rendered_sections
    assert "Low-value related link" not in rendered_sections


def test_parser_marks_lore_namespace_when_no_specific_type_matches() -> None:
    html = """
    <html>
      <body>
        <h1 id="firstHeading">Dragons</h1>
        <div id="mw-content-text">
          <div class="mw-parser-output">
            <p>Dragons are ancient beings tied to Akatosh.</p>
          </div>
        </div>
      </body>
    </html>
    """

    document = UespParser().parse(
        html,
        source_url="https://en.uesp.net/wiki/Lore:Dragons",
        retrieved_at=datetime(2024, 1, 1, tzinfo=UTC),
    )

    assert document.namespace == "Lore"
    assert document.entity_type == "lore"


def test_parser_ignores_decomposed_styled_children_inside_noise_blocks() -> None:
    html = """
    <html>
      <body>
        <h1 id="firstHeading">Styled Noise</h1>
        <div id="mw-content-text">
          <div class="mw-parser-output">
            <div class="navbox">
              <span style="display:none">Already removed with parent</span>
            </div>
            <p>Useful content remains.</p>
          </div>
        </div>
      </body>
    </html>
    """

    document = UespParser().parse(
        html,
        source_url="https://en.uesp.net/wiki/Skyrim:Styled_Noise",
        retrieved_at=datetime(2024, 1, 1, tzinfo=UTC),
    )

    rendered_sections = "\n\n".join(section.markdown for section in document.sections)

    assert "Useful content remains." in rendered_sections
    assert "Already removed with parent" not in rendered_sections
