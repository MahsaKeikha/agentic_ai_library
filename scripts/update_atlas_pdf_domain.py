#!/usr/bin/env python3
"""Align the published Atlas PDF with the canonical public domain."""

from pathlib import Path
import shutil

import fitz
from pypdf import PdfReader, PdfWriter


OLD_BASE = "https://mahsakeikha.github.io/agentic_ai_library/"
NEW_BASE = "https://multiagentaiatlas.com/"

# Each entry is old display text, new display text, link destination, hit index.
EDITS = {
    2: [(OLD_BASE.removeprefix("https://"), NEW_BASE.removeprefix("https://"), NEW_BASE, 0)],
    45: [
        (OLD_BASE + "demo-lab.html", NEW_BASE + "demo-lab.html", NEW_BASE + "demo-lab.html", 0),
        (OLD_BASE + "atlas-demo-lab-social-preview.png", NEW_BASE + "atlas-demo-lab-social-preview.png", NEW_BASE + "atlas-demo-lab-social-preview.png", 0),
        (OLD_BASE + "atlas-demo-lab-social-preview.png", NEW_BASE + "atlas-demo-lab-social-preview.png", NEW_BASE + "atlas-demo-lab-social-preview.png", 1),
        (OLD_BASE + "demo-lab.html", NEW_BASE + "demo-lab.html", NEW_BASE + "demo-lab.html", 1),
    ],
    46: [
        (OLD_BASE + "atlas-demo-lab-social-preview.png", NEW_BASE + "atlas-demo-lab-social-preview.png", NEW_BASE + "atlas-demo-lab-social-preview.png", 0),
        (OLD_BASE + "demo-lab.html", NEW_BASE + "demo-lab.html", NEW_BASE + "demo-lab.html", 0),
    ],
    68: [
        (OLD_BASE, NEW_BASE, NEW_BASE, 0),
        (OLD_BASE + "atlas.html", NEW_BASE + "atlas.html", NEW_BASE + "atlas.html", 0),
        (OLD_BASE + "flagships.html", NEW_BASE + "flagships.html", NEW_BASE + "flagships.html", 0),
        (OLD_BASE + "demo-lab.html", NEW_BASE + "demo-lab.html", NEW_BASE + "demo-lab.html", 0),
        (OLD_BASE + "evidence.html", NEW_BASE + "evidence.html", NEW_BASE + "evidence.html", 0),
        (OLD_BASE + "about.html", NEW_BASE + "about.html", NEW_BASE + "about.html", 0),
        (OLD_BASE + "training.html", NEW_BASE + "training.html", NEW_BASE + "training.html", 0),
        (OLD_BASE + "founding-partners.html", NEW_BASE + "founding-partners.html", NEW_BASE + "founding-partners.html", 0),
    ],
}


def span_style(page: fitz.Page, rect: fitz.Rect) -> tuple[str, float, tuple[float, float, float]]:
    for block in page.get_text("dict")["blocks"]:
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                if fitz.Rect(span["bbox"]).intersects(rect):
                    source_font = span["font"].lower()
                    if "dejavu" in source_font:
                        font = "dejavu"
                    elif "mono" in source_font or "cour" in source_font:
                        font = "cour"
                    else:
                        font = "helv"
                    value = span.get("color", 0)
                    color = ((value >> 16 & 255) / 255, (value >> 8 & 255) / 255, (value & 255) / 255)
                    return font, float(span["size"]), color
    return "helv", max(7.0, rect.height * 0.78), (0, 0, 0)


def background_color(page: fitz.Page, rect: fitz.Rect) -> tuple[float, float, float]:
    pixmap = page.get_pixmap(matrix=fitz.Matrix(1, 1), colorspace=fitz.csRGB, alpha=False)
    x = min(pixmap.width - 1, max(0, round(rect.x0 + 3)))
    y = min(pixmap.height - 1, max(0, round(rect.y0 - 2)))
    red, green, blue = pixmap.pixel(x, y)[:3]
    return red / 255, green / 255, blue / 255


def update_pdf(source: Path, output: Path) -> None:
    work = output.with_suffix(".layout.pdf")
    document = fitz.open(source)
    replaced = 0

    for page_number, edits in EDITS.items():
        page = document[page_number - 1]
        prepared = []
        for old_text, new_text, target, hit_index in edits:
            hits = sorted(page.search_for(old_text), key=lambda item: (item.y0, item.x0))
            if hit_index >= len(hits):
                raise RuntimeError(f"Page {page_number}: could not locate {old_text!r} hit {hit_index}")
            rect = hits[hit_index]
            prepared.append((rect, span_style(page, rect), background_color(page, rect), new_text, target))

        for rect, _, background, _, _ in prepared:
            page.add_redact_annot(rect, fill=background)
        page.apply_redactions()

        for rect, (font, size, color), _, new_text, target in prepared:
            if font == "dejavu":
                page.insert_font(fontname="dejavu", fontfile="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
            page.insert_text(
                fitz.Point(rect.x0, rect.y1 - 1.2),
                new_text,
                fontname=font,
                fontsize=size,
                color=color,
                overlay=True,
            )
            if font == "dejavu":
                replacement_width = fitz.Font(fontfile="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf").text_length(new_text, fontsize=size)
            else:
                replacement_width = fitz.get_text_length(new_text, fontname=font, fontsize=size)
            link_rect = fitz.Rect(rect.x0, rect.y0, rect.x0 + replacement_width, rect.y1)
            page.insert_link({"kind": fitz.LINK_URI, "from": link_rect, "uri": target})
            replaced += 1

    if replaced != 15:
        raise RuntimeError(f"Expected 15 replacements, completed {replaced}")

    document.save(work, garbage=4, deflate=True)
    document.close()

    reader = PdfReader(work)
    writer = PdfWriter()
    writer.clone_document_from_reader(reader)
    metadata = {str(k): str(v) for k, v in (reader.metadata or {}).items() if v is not None}
    metadata.update(
        {
            "/Title": "The Multi-Agent AI Atlas",
            "/Author": "Mahsa Keikha, PhD, P.Eng.",
            "/Subject": "The official field guide to the Multi-Agent AI Atlas",
            "/Website": "https://multiagentaiatlas.com/",
            "/SourceRepository": "https://github.com/MahsaKeikha/agentic_ai_library",
        }
    )
    writer.add_metadata(metadata)
    with output.open("wb") as stream:
        writer.write(stream)
    work.unlink()


if __name__ == "__main__":
    source_pdf = Path("docs/books/The_Multi_Agent_AI_Atlas.pdf")
    backup_pdf = Path("tmp/pdfs/The_Multi_Agent_AI_Atlas.before-domain-update.pdf")
    backup_pdf.parent.mkdir(parents=True, exist_ok=True)
    if not backup_pdf.exists():
        shutil.copy2(source_pdf, backup_pdf)
    update_pdf(backup_pdf, source_pdf)
