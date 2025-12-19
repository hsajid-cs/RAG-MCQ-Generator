import argparse
import re
from pathlib import Path
from typing import Iterable

from mistralai import DocumentURLChunk, Mistral
from mistralai.models import OCRResponse

DEFAULT_MODEL = "mistral-ocr-latest"
DEFAULT_INPUT_DIR = Path("data")
DEFAULT_OUTPUT_DIR = Path("data_raw")
DEFAULT_API_KEY = "kqUXzszw1ir3P1ZBg5F3QookOKSafG39"


def create_mistral_client() -> Mistral:
    """Create a Mistral client instance using the inline API key."""
    return Mistral(api_key=DEFAULT_API_KEY)


def get_combined_markdown(ocr_response: OCRResponse) -> str:
    """Combine OCR text into a single markdown document without image placeholders."""
    markdown_pages: list[str] = []
    for page in ocr_response.pages:
        page_markdown = re.sub(r"!\[.*?\]\(.*?\)", "[Image removed]", page.markdown)
        markdown_pages.append(page_markdown)
    return "\n\n".join(markdown_pages)


def process_pdf_file(pdf_path: Path, output_path: Path, client: Mistral, *, model: str, force: bool) -> bool:
    """Convert a single PDF file to markdown, respecting cache and force options."""
    if output_path.exists() and not force:
        return False

    uploaded_file = client.files.upload(
        file={"file_name": pdf_path.stem, "content": pdf_path.read_bytes()},
        purpose="ocr",
    )
    signed_url = client.files.get_signed_url(file_id=uploaded_file.id, expiry=1)

    pdf_response = client.ocr.process(
        document=DocumentURLChunk(document_url=signed_url.url),
        model=model,
        include_image_base64=False,
    )

    combined_markdown = get_combined_markdown(pdf_response)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(combined_markdown, encoding="utf-8")
    return True


def iter_pdf_files(pdf_dir: Path) -> Iterable[Path]:
    """Yield all PDF files under the provided directory."""
    return pdf_dir.rglob("*.pdf")


def process_all_pdfs(
    *,
    input_dir: Path,
    output_dir: Path,
    client: Mistral,
    model: str = DEFAULT_MODEL,
    force: bool = False,
) -> None:
    """Process all PDFs discovered under the input directory."""
    pdf_files = list(iter_pdf_files(input_dir))
    if not pdf_files:
        print(f"No PDF files found in {input_dir}!")
        return

    print(f"Found {len(pdf_files)} PDF file(s) to process\n")
    print("=" * 60)

    processed_count = skipped_count = error_count = 0

    for idx, pdf_path in enumerate(pdf_files, 1):
        relative_path = pdf_path.relative_to(input_dir)
        output_path = output_dir / relative_path.with_suffix(".md")

        print(f"\n[{idx}/{len(pdf_files)}] File: {pdf_path.name}")
        print(f"    Source: {relative_path}")
        print(f"    Output: {output_path}")

        try:
            if process_pdf_file(pdf_path, output_path, client, model=model, force=force):
                print("    Status: Successfully processed")
                processed_count += 1
            else:
                print("    Status: Skipped (already exists)")
                skipped_count += 1
        except Exception as exc:  # pylint: disable=broad-except
            print(f"    Status: Error - {exc}")
            error_count += 1

        print("-" * 60)

    print("\n" + "=" * 60)
    print("SUMMARY:")
    print(f"  Total files found: {len(pdf_files)}")
    print(f"  Processing done: {processed_count}")
    print(f"  Documents skipped count: {skipped_count}")
    print(f"  Error count: {error_count}")
    print("=" * 60)


def build_parser() -> argparse.ArgumentParser:
    """Create the argument parser for the CLI."""
    parser = argparse.ArgumentParser(description="Convert PDFs to markdown via Mistral OCR")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT_DIR, help="Directory containing PDFs")
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Directory to write generated markdown files",
    )
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Mistral OCR model name")
    parser.add_argument("--force", action="store_true", help="Reprocess files even if markdown exists")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    client = create_mistral_client()

    process_all_pdfs(
        input_dir=args.input,
        output_dir=args.output,
        client=client,
        model=args.model,
        force=args.force,
    )

    print("\n✓ All PDF files processed!")


if __name__ == "__main__":
    main()
