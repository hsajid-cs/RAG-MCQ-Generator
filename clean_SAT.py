from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import List

# ---------------------------------------------------------------------------
# Globals
# ---------------------------------------------------------------------------

CORPUS_DIR = Path("corpus")
BLUEPRINT_DIR = Path("blueprint")

# Markers for start and end sections to remove
START_MARKER = "# SAT Writing Cheat Sheet"
END_MARKER = "# ABOUT THE AUTHOR"

# Remove inline elements
INLINE_DROP = (
    (re.compile(r"\[Image removed\]\s*", re.IGNORECASE), ""),
    (re.compile(r"■THE CRITICAL READER\s*\n?", re.IGNORECASE), ""),
    (re.compile(r"t\.me/SAT_files\s*\n?", re.IGNORECASE), ""),
)

# Clean up formatting
PAGE_NUM = re.compile(r"^\s*\d{1,3}\s*$", re.MULTILINE)
MULTI_NL = re.compile(r"\n{3,}")
END_SPACE = re.compile(r" +\n")

# Chapter pattern for SAT English (numbered chapters)
MD_CHAPTER_PATTERN = re.compile(
    r"^#\s*(\d+)\.\s+(.+?)\s*\.{5}\s*\d+\s*$",
    re.MULTILINE
)

# Topic/section pattern (## headings)
MD_TOPIC_HEAD = re.compile(r"^(#{2,3})\s+(.+?)\s*$", re.MULTILINE)

SKIP_HEADINGS = {
    "learning objective",
    "learning objectives", 
    "objectives",
    "answers",
    "answer key",
    "exercise",
    "exercises",
    "summary",
    "summaries",
    "review questions",
    "review",
    "glossary",
    "assessment",
    "and two general points",
}

# ---------------------------------------------------------------------------
# Data Models
# ---------------------------------------------------------------------------

@dataclass
class Topic:
    index: int
    title: str
    text: str
    level: int
    rel_path: str | None = None


@dataclass
class Chapter:
    key: str
    number: str
    title: str
    body: str
    topics: List[Topic] = field(default_factory=list)


# ---------------------------------------------------------------------------
# FS setup
# ---------------------------------------------------------------------------

def setup_dirs() -> None:
    sat_dir = CORPUS_DIR / "sat_english"
    sat_dir.mkdir(parents=True, exist_ok=True)
    BLUEPRINT_DIR.mkdir(parents=True, exist_ok=True)
    print("Directory structure ready")


# ---------------------------------------------------------------------------
# Cleaning
# ---------------------------------------------------------------------------

def tidy_markdown(raw: str) -> str:
    """Remove boilerplate, author info, and clean up formatting."""
    
    # Fast approach: find start and end markers, keep only the content in between
    start_idx = raw.find(START_MARKER)
    if start_idx != -1:
        # Keep from "# SAT Writing Cheat Sheet" onwards
        raw = raw[start_idx:]
    
    end_idx = raw.find(END_MARKER)
    if end_idx != -1:
        # Remove "# ABOUT THE AUTHOR" and everything after
        raw = raw[:end_idx]
    
    # Remove inline elements (fast, simple patterns)
    for pat, repl in INLINE_DROP:
        raw = pat.sub(repl, raw)
    
    # Clean up formatting
    raw = PAGE_NUM.sub("", raw)
    raw = MULTI_NL.sub("\n\n", raw)
    raw = END_SPACE.sub("\n", raw)
    
    return raw.strip()


# ---------------------------------------------------------------------------
# Chapter & topic extraction
# ---------------------------------------------------------------------------

def find_chapters(text: str) -> List[Chapter]:
    """Extract chapters from SAT English content."""
    chapters = []
    
    # Find all chapter headings from table of contents pattern
    matches = list(MD_CHAPTER_PATTERN.finditer(text))
    
    if not matches:
        print("No chapters found with TOC pattern, creating single chapter")
        # If no chapters found, treat entire content as one chapter
        chapters.append(
            Chapter(
                key="sat_english_ch0_content",
                number="0",
                title="SAT English Content",
                body=text
            )
        )
        return chapters
    
    # Process each chapter
    for i, match in enumerate(matches):
        num = match.group(1)
        title = match.group(2).strip()
        
        # Find the start of actual chapter content (look for the chapter number as heading)
        chapter_heading_pattern = re.compile(
            rf"^#\s*{re.escape(num)}\.?\s+{re.escape(title)}",
            re.MULTILINE | re.IGNORECASE
        )
        
        content_matches = list(chapter_heading_pattern.finditer(text))
        if not content_matches:
            continue
            
        start = content_matches[0].start()
        
        # Find end (start of next chapter or end of text)
        if i + 1 < len(matches):
            next_num = matches[i + 1].group(1)
            next_title = matches[i + 1].group(2).strip()
            next_pattern = re.compile(
                rf"^#\s*{re.escape(next_num)}\.?\s+{re.escape(next_title)}",
                re.MULTILINE | re.IGNORECASE
            )
            next_matches = list(next_pattern.finditer(text))
            end = next_matches[0].start() if next_matches else len(text)
        else:
            end = len(text)
        
        chunk = text[start:end].strip()
        
        # Create clean key
        base = re.sub(r"[^\w\s-]", "", title)
        base = re.sub(r"\s+", "_", base).lower()[:40]
        key = f"sat_english_ch{num}_{base}"
        
        chapters.append(
            Chapter(
                key=key,
                number=num,
                title=title,
                body=chunk
            )
        )
    
    return chapters


def split_topics(text: str, fallback_title: str) -> List[Topic]:
    """Split chapter into topics based on headings."""
    heads = list(MD_TOPIC_HEAD.finditer(text))
    
    if not heads:
        return [Topic(index=1, title=fallback_title, text=text.strip(), level=1)]
    
    out: List[Topic] = []
    
    for i, h in enumerate(heads):
        ttl = h.group(2).strip().lower()
        
        # Skip certain headings
        if ttl in SKIP_HEADINGS:
            continue
        
        start = h.start()
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        block = text[start:end].strip()
        
        if not block or len(block) < 50:  # Skip very short sections
            continue
        
        out.append(
            Topic(
                index=len(out) + 1,
                title=h.group(2).strip(),
                text=block,
                level=len(h.group(1)),
            )
        )
    
    if not out:
        return [Topic(index=1, title=fallback_title, text=text.strip(), level=1)]
    
    return out


# ---------------------------------------------------------------------------
# Persistence
# ---------------------------------------------------------------------------

def make_slug(txt: str, fallback: str, limit: int = 50) -> str:
    """Create a filesystem-safe slug from text."""
    base = re.sub(r"[^a-zA-Z0-9]+", "-", txt.strip()).strip("-").lower()
    base = base[:limit].strip("-")
    return base or fallback


def save_chapter(ch: Chapter, root: Path) -> None:
    """Save chapter and its topics to filesystem."""
    folder = root / ch.key
    folder.mkdir(parents=True, exist_ok=True)
    
    # Save full chapter
    (folder / "000_chapter.md").write_text(ch.body, encoding="utf-8")
    
    # Save individual topics
    for t in ch.topics:
        slug = make_slug(t.title, f"topic-{t.index:03d}")
        name = f"{t.index:03d}_{slug}.md"
        path = folder / name
        path.write_text(t.text, encoding="utf-8")
        t.rel_path = path.relative_to(CORPUS_DIR).as_posix()


# ---------------------------------------------------------------------------
# Blueprint generation
# ---------------------------------------------------------------------------

def build_blueprint(chapters: List[Chapter]) -> None:
    """Generate blueprint.json for SAT English content."""
    bp = {
        "project_info": {
            "name": "SAT English Grammar & Writing",
            "subject": "SAT English",
            "source": "The Ultimate Guide to SAT Grammar by Erica Meltzer",
        },
        "structure": {
            "sat_english": {}
        },
    }
    
    for ch in chapters:
        bp["structure"]["sat_english"][f"Chapter {ch.number}"] = {
            "title": ch.title,
            "chapter_id": ch.key,
            "topics": [
                {
                    "title": t.title,
                    "file": t.rel_path or "",
                    "heading_level": t.level
                }
                for t in ch.topics
            ],
        }
    
    blueprint_path = BLUEPRINT_DIR / "blueprint_sat_english.json"
    blueprint_path.write_text(
        json.dumps(bp, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"Blueprint generated: {blueprint_path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    """Main processing function."""
    print("Starting SAT English cleanup and chunking...")
    
    setup_dirs()
    
    # Read raw file
    src_path = Path("data_raw") / "SAT_English.md"
    if not src_path.exists():
        print(f"Error: {src_path} not found!")
        return
    
    print(f"Reading {src_path}...")
    raw_text = src_path.read_text(encoding="utf-8")
    
    # Clean the text
    print("Cleaning text (removing boilerplate, authors, etc.)...")
    clean_text = tidy_markdown(raw_text)
    
    # Save cleaned version
    clean_path = Path("data") / "SAT_English_cleaned.md"
    clean_path.parent.mkdir(parents=True, exist_ok=True)
    clean_path.write_text(clean_text, encoding="utf-8")
    print(f"Cleaned text saved to {clean_path}")
    
    # Extract chapters
    print("Extracting chapters...")
    chapters = find_chapters(clean_text)
    print(f"Found {len(chapters)} chapters")
    
    # Process each chapter
    dest_root = CORPUS_DIR / "sat_english"
    for ch in chapters:
        print(f"Processing Chapter {ch.number}: {ch.title}")
        ch.topics = split_topics(ch.body, ch.title)
        save_chapter(ch, dest_root)
        print(f"  ✓ Saved {len(ch.topics)} topics")
    
    # Generate blueprint
    build_blueprint(chapters)
    
    print("\n✅ SAT English processing complete!")
    print(f"   - Cleaned file: {clean_path}")
    print(f"   - Corpus: {dest_root}")
    print(f"   - Total chapters: {len(chapters)}")
    print(f"   - Total topics: {sum(len(ch.topics) for ch in chapters)}")


if __name__ == "__main__":
    main()
