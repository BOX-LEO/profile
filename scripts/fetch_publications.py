"""Fetch publications from Google Scholar and write publications.json.

Usage:
    pip install scholarly
    python scripts/fetch_publications.py

Re-run whenever you want to refresh the publication list.
"""

import json
import sys
from pathlib import Path

from scholarly import scholarly

SCHOLAR_ID = "hgQiMmgAAAAJ"
OUTPUT = Path(__file__).resolve().parent.parent / "publications.json"


MANUAL_FIELDS = ("code", "image", "projectpage", "huggingface")


def load_existing() -> dict:
    if not OUTPUT.exists():
        return {}
    try:
        data = json.loads(OUTPUT.read_text())
    except json.JSONDecodeError:
        return {}
    return {p.get("title", "").strip().lower(): p for p in data if p.get("title")}


def main() -> int:
    existing = load_existing()

    print(f"Fetching author {SCHOLAR_ID}...")
    author = scholarly.search_author_id(SCHOLAR_ID)
    author = scholarly.fill(author, sections=["publications"])

    pubs = []
    for i, pub in enumerate(author["publications"], 1):
        print(f"  [{i}/{len(author['publications'])}] filling: {pub['bib'].get('title', '?')[:70]}")
        filled = scholarly.fill(pub)
        bib = filled.get("bib", {})
        title = bib.get("title", "")
        prior = existing.get(title.strip().lower(), {})

        entry = {
            "title": title,
            "authors": bib.get("author", ""),
            "venue": bib.get("venue") or bib.get("journal") or bib.get("conference") or "",
            "year": bib.get("pub_year", ""),
            "abstract": bib.get("abstract", ""),
            "url": filled.get("pub_url") or "",
            "citations": filled.get("num_citations", 0),
        }
        for field in MANUAL_FIELDS:
            entry[field] = prior.get(field, "")
        pubs.append(entry)

    pubs.sort(key=lambda p: (str(p.get("year") or ""), p.get("citations", 0)), reverse=True)

    OUTPUT.write_text(json.dumps(pubs, indent=2, ensure_ascii=False))
    print(f"\nWrote {len(pubs)} publications to {OUTPUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
