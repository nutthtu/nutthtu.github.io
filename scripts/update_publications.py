#!/usr/bin/env python3
"""
Update data/publications.json from a BibTeX file (e.g. a Zotero export).

Usage
-----
  # Default: reads data/publications.bib
  python scripts/update_publications.py

  # Or point at any .bib file:
  python scripts/update_publications.py --bib Tuchinda.bib

Each publication title on the website links to https://doi.org/<doi> when the entry
has a `doi` field, and falls back to the entry's `url` otherwise.

Dependencies (install once)
---------------------------
  pip install bibtexparser
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from datetime import date


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = ROOT / "data" / "publications.json"
DEFAULT_BIB = ROOT / "data" / "publications.bib"

MONTHS = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}


# ----------------- BibTeX -----------------

def fetch_from_bibtex(bib_path: Path) -> list[dict]:
    try:
        import bibtexparser
        from bibtexparser.bparser import BibTexParser
        from bibtexparser.customization import convert_to_unicode
    except ImportError:
        sys.exit("bibtexparser not installed.  pip install bibtexparser")

    parser = BibTexParser(common_strings=True)
    parser.customization = convert_to_unicode
    db = bibtexparser.loads(bib_path.read_text(encoding="utf-8"), parser=parser)

    out: list[dict] = []
    for e in db.entries:
        title = _clean(e.get("title", ""))
        if not title:
            continue
        doi = _clean_doi(e.get("doi", ""))
        url = _clean(e.get("url", ""))
        if re.match(r"https?://", doi):  # a non-DOI link (e.g. a Handle) stored in the doi field
            url, doi = url or doi, ""
        out.append({
            "title": title,
            "authors": _format_authors(e.get("author", "")),
            "venue": _clean(e.get("journal", "") or e.get("booktitle", "") or e.get("publisher", "")),
            "year": _int_or_none(e.get("year", "")),
            "month": _month(e.get("month", "")),
            "doi": doi,
            "url": f"https://doi.org/{doi}" if doi else url,
        })
    return out


def _clean(s: str) -> str:
    s = re.sub(r"[{}]", "", s)
    s = s.replace("\\&", "&").replace("\\%", "%")
    return re.sub(r"\s+", " ", s).strip()


def _clean_doi(s: str) -> str:
    s = _clean(s)
    return re.sub(r"^(https?://(dx\.)?doi\.org/|doi:)", "", s, flags=re.I)


def _format_authors(s: str) -> str:
    """'Tuchinda, Nutth and Schuh, Christopher A.' -> 'Nutth Tuchinda, Christopher A. Schuh'"""
    names = []
    for a in re.split(r"\s+and\s+", _clean(s)):
        if "," in a:
            last, first = [x.strip() for x in a.split(",", 1)]
            a = f"{first} {last}".strip()
        if a:
            names.append(a)
    return ", ".join(names)


def _month(s) -> int | None:
    s = str(s).strip().lower()
    if s.isdigit():
        return int(s)
    return MONTHS.get(s[:3])


def _int_or_none(s):
    m = re.search(r"\d{4}", str(s))
    return int(m.group()) if m else None


# ----------------- CLI -----------------

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--bib", type=Path, default=DEFAULT_BIB,
                    help=f"Path to a BibTeX file (default: {DEFAULT_BIB.relative_to(ROOT)})")
    args = ap.parse_args()

    if not args.bib.exists():
        ap.error(f"BibTeX file not found: {args.bib}")

    pubs = fetch_from_bibtex(args.bib)
    pubs.sort(key=lambda p: (p.get("year") or 0, p.get("month") or 0), reverse=True)

    missing = [p["title"] for p in pubs if not p["url"]]
    for t in missing:
        print(f"  ! no DOI or URL (title will not be linked): {t}")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({
        "meta": {
            "updated": date.today().isoformat(),
            "source": "bibtex",
            "count": len(pubs),
        },
        "publications": pubs,
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"[done] wrote {len(pubs)} publications → {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
