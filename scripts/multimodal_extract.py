#!/usr/bin/env python3
"""
PDF Complexity Assessment & OCR Routing for LLM Wiki.

Assess PDF text density to decide:
- proceed: normal processing (fitz text extract)
- direct_ocr: RapidOCR sufficient (file ≤10MB, density <10%)
- vlm: needs VLM (file >10MB, density still <10% after OCR) — rare for searchable PDFs

Usage:
    python multimodal_extract.py --file <path>
"""

import argparse
import json
import os
import sys

TEXT_DENSITY_THRESHOLD = 0.10  # 10%
PDF_SIZE_THRESHOLD_MB = 10
REFERENCE_CHARS_PER_PAGE = 1500  # Chinese doc average

def assess_pdf_complexity(file_path: str) -> dict:
    """
    Returns:
      - is_scanned_or_complex: bool
      - text_density: float
      - recommendation: "proceed" | "direct_ocr" | "vlm"
    """
    file_size_mb = os.path.getsize(file_path) / (1024 * 1024)

    try:
        import fitz
        doc = fitz.open(file_path)
        total_chars = 0
        total_pages = len(doc)
        for page in doc:
            total_chars += len(page.get_text())
        doc.close()
    except Exception as e:
        return {
            "file_size_mb": round(file_size_mb, 2),
            "total_chars": 0,
            "total_pages": 0,
            "text_density": 0.0,
            "is_scanned_or_complex": True,
            "recommendation": "direct_ocr",
            "error": str(e)
        }

    text_density = total_chars / (total_pages * REFERENCE_CHARS_PER_PAGE) if total_pages > 0 else 0.0

    if file_size_mb > PDF_SIZE_THRESHOLD_MB and text_density < TEXT_DENSITY_THRESHOLD:
        recommendation = "vlm"
    elif text_density < TEXT_DENSITY_THRESHOLD:
        recommendation = "direct_ocr"
    else:
        recommendation = "proceed"

    return {
        "file_size_mb": round(file_size_mb, 2),
        "total_chars": total_chars,
        "total_pages": total_pages,
        "text_density": round(text_density, 3),
        "is_scanned_or_complex": recommendation in ("direct_ocr", "vlm"),
        "recommendation": recommendation
    }

def extract_with_rapidocr(file_path: str) -> str:
    """Extract text from PDF using RapidOCR."""
    try:
        from rapidocr import RapidOCR
        ocr = RapidOCR()
        result, elapsed = ocr(file_path)
        if result:
            lines = []
            for line in result:
                # line format: [box, text, score]
                lines.append(line[1])
            return '\n'.join(lines)
        return ""
    except Exception as e:
        return f"[RapidOCR failed: {e}]"

def extract_text(file_path: str, force_ocr: bool = False) -> dict:
    """
    Main extraction function. Returns dict with text and metadata.
    """
    ext = os.path.splitext(file_path)[1].lower()

    if ext == '.pdf':
        assessment = assess_pdf_complexity(file_path)
        text = ""

        if force_ocr or assessment['recommendation'] == 'direct_ocr':
            text = extract_with_rapidocr(file_path)
            assessment['extraction_method'] = 'rapidocr'
        elif assessment['recommendation'] == 'vlm':
            # Rare case — for Lei Ge's docs this almost never happens
            assessment['extraction_method'] = 'vlm_needed'
            text = ""
        else:
            # Normal: fitz text extract
            import fitz
            doc = fitz.open(file_path)
            for page in doc:
                text += page.get_text()
            doc.close()
            assessment['extraction_method'] = 'fitz'

        return {
            "text": text,
            "assessment": assessment
        }

    else:
        # Non-PDF: handled elsewhere in ingest pipeline
        return {
            "text": "",
            "assessment": {
                "recommendation": "not_pdf",
                "is_scanned_or_complex": False
            }
        }

def main():
    parser = argparse.ArgumentParser(description='PDF complexity assessment & extraction')
    parser.add_argument('--file', required=True, help='Path to PDF file')
    parser.add_argument('--extract', action='store_true', help='Also extract text')
    parser.add_argument('--force-ocr', action='store_true', help='Force RapidOCR extraction')
    args = parser.parse_args()

    if args.extract:
        result = extract_text(args.file, force_ocr=args.force_ocr)
    else:
        result = assess_pdf_complexity(args.file)

    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
