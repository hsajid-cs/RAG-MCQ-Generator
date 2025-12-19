from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Iterator, Mapping, Tuple

# ---------------------------------------------------------------------------
# Globals
# ---------------------------------------------------------------------------

CORPUS_DIR = Path("corpus")
topic_blueprint_DIR = Path("topic_blueprint")

MD_CHAPTER_START = re.compile(r"(#{1,2}\s*(?:Chapter|CHAPTER)\s+\d+)")
MD_topic_blueprint_HEAD = re.compile(r"^(#{2,4})\s+(.+?)\s*$", re.MULTILINE)

MD_CHAPTER_PATTERNS = (
    re.compile(
        r"#{1,2}\s*(Chapter|CHAPTER)\s+(\d+)\s*\n+#{1,3}\s*(.+?)(?=\n#{1,2}\s*(?:Chapter|CHAPTER)\s+\d+|\Z)",
        re.DOTALL,
    ),
    re.compile(
        r"#\s*(CHAPTER|Chapter)\s*\n+#{1,3}\s*(\d+)\s*\n+#{1,3}\s*(.+?)(?=\n#\s*(?:CHAPTER|Chapter)\s*|\Z)",
        re.DOTALL,
    ),
)

REMOVALS = (
    re.compile(r"#\s*Authors?\s*\n.*?(?=\n#|\Z)", re.DOTALL),
    re.compile(r"#\s*Reviewers?\s*\n.*?(?=\n#|\Z)", re.DOTALL),
    re.compile(r"#\s*Editors?\s*\n.*?(?=\n#|\Z)", re.DOTALL),
    re.compile(r"#\s*(?:CONTENTS|Table of Contents|Contents)\s*\n.*?(?=\n#|\Z)", re.DOTALL),
    re.compile(r".*?(PUNJAB EDUCATION|All rights are reserved|copyright).*?\n", re.IGNORECASE),
    re.compile(r"#\s*\(In the Name of.*?\)\s*\n", re.IGNORECASE),
    re.compile(r"#\s*Bibliography.*", re.DOTALL),
)

INLINE_DROP = (
    (re.compile(r"\[Image removed\]\s*", re.IGNORECASE), ""),
    (re.compile(r"Do you know\?\s*\n\s*\n", re.IGNORECASE), ""),
    (re.compile(r"For Your Information\s*\n\s*\n", re.IGNORECASE), ""),
    (re.compile(r"Interesting Information\s*\n\s*\n", re.IGNORECASE), ""),
    (re.compile(r"Point to Ponder\s*\n\s*\n", re.IGNORECASE), ""),
    (re.compile(r"Challenge:\s*\n\s*\n"), ""),
)

PAGE_NUM = re.compile(r"^\s*\d{1,3}\s*$", re.MULTILINE)
MULTI_NL = re.compile(r"\n{3,}")
END_SPACE = re.compile(r" +\n")

SKIP_HEADINGS = {
    "learning objective",
    "learning objectives",
    "objectives",
    "answers",
    "exercise",
    "exercises",
    "summary",
    "summaries",
    "review questions",
    "review",
    "glossary",
    "assessment",
}

# ---------------------------------------------------------------------------
# Data Models
# ---------------------------------------------------------------------------

@dataclass
class topic_blueprint:
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
    topic_blueprints: List[topic_blueprint] = field(default_factory=list)


@dataclass
class Record:
    chapter: Chapter
    grade: str
    subject: str
    corpus_key: str
    blue_key: str


@dataclass(frozen=True)
class SubjectInfo:
    subject: str
    corpus: str
    blue: str
    files: Tuple[str, ...]


# ---------------------------------------------------------------------------
# FS setup
# ---------------------------------------------------------------------------

def setup_dirs() -> None:
    for p in [CORPUS_DIR / "physics", CORPUS_DIR / "math", topic_blueprint_DIR]:
        p.mkdir(parents=True, exist_ok=True)
    print("Directory structure ready")


# ---------------------------------------------------------------------------
# Cleaning
# ---------------------------------------------------------------------------

def tidy_markdown(raw: str) -> str:
    start = MD_CHAPTER_START.search(raw)
    if start:
        raw = raw[start.start():]

    for pat in REMOVALS:
        raw = pat.sub("", raw)

    for pat, repl in INLINE_DROP:
        raw = pat.sub(repl, raw)

    raw = PAGE_NUM.sub("", raw)
    raw = MULTI_NL.sub("\n\n", raw)
    raw = END_SPACE.sub("\n", raw)

    return raw.strip()


# ---------------------------------------------------------------------------
# Chapter & topic_blueprint extraction
# ---------------------------------------------------------------------------

def find_chapters(text: str, label: str) -> List[Chapter]:
    points = []
    for pat in MD_CHAPTER_PATTERNS:
        found = list(pat.finditer(text))
        if found:
            points = found
            break

    result = []
    for i, m in enumerate(points):
        num = m.group(2)
        title = m.group(3).strip()
        start = m.start()
        end = points[i+1].start() if i + 1 < len(points) else len(text)
        chunk = text[start:end].strip()

        base = re.sub(r"[^\w\s-]", "", title)
        base = re.sub(r"\s+", "_", base).lower()[:30]
        token = base or "chapter"
        key = f"{label.lower()}_ch{num}_{token}"

        result.append(Chapter(key=key, number=num, title=title, body=chunk))

    return result


def scan_topic_blueprint_heads(text: str) -> Iterator[re.Match]:
    return MD_topic_blueprint_HEAD.finditer(text)


def split_topic_blueprints(text: str, fallback_title: str) -> List[topic_blueprint]:
    heads = list(scan_topic_blueprint_heads(text))
    if not heads:
        return [topic_blueprint(index=1, title=fallback_title, text=text.strip(), level=1)]

    deep = any(len(h.group(1)) >= 3 for h in heads)
    chosen = [h for h in heads if not deep or len(h.group(1)) >= 3]

    out: List[topic_blueprint] = []
    for i, h in enumerate(chosen):
        ttl = h.group(2).strip().lower()
        if ttl in SKIP_HEADINGS:
            continue

        start = h.start()
        end = chosen[i+1].start() if i + 1 < len(chosen) else len(text)
        block = text[start:end].strip()
        if not block:
            continue

        out.append(
            topic_blueprint(
                index=len(out)+1,
                title=h.group(2).strip(),
                text=block,
                level=len(h.group(1)),
            )
        )

    if not out:
        return [topic_blueprint(index=1, title=fallback_title, text=text.strip(), level=1)]

    return out


# ---------------------------------------------------------------------------
# Persistence
# ---------------------------------------------------------------------------

def make_slug(txt: str, fallback: str, limit: int = 50) -> str:
    base = re.sub(r"[^a-zA-Z0-9]+", "-", txt.strip()).strip("-").lower()
    base = base[:limit].strip("-")
    return base or fallback


def save_chapter(ch: Chapter, root: Path, grade: str) -> None:
    folder = root / f"grade_{grade}" / ch.key
    folder.mkdir(parents=True, exist_ok=True)

    (folder / "000_chapter.md").write_text(ch.body, encoding="utf-8")

    for t in ch.topic_blueprints:
        slug = make_slug(t.title, f"topic_blueprint-{t.index:03d}")
        name = f"{t.index:03d}_{slug}.md"
        path = folder / name
        path.write_text(t.text, encoding="utf-8")
        t.rel_path = path.relative_to(CORPUS_DIR).as_posix()


# ---------------------------------------------------------------------------
# Subject processing
# ---------------------------------------------------------------------------

def run_subject(info: SubjectInfo, src: Path) -> Dict[str, Record]:
    print(f"Processing {info.subject}")
    records: Dict[str, Record] = {}
    dest = CORPUS_DIR / info.corpus

    for fname in info.files:
        fpath = src / fname
        if not fpath.exists():
            print(f"Missing: {fname}")
            continue

        text = tidy_markdown(fpath.read_text(encoding="utf-8"))
        grade = "11" if "11" in fname else "12"

        chapters = find_chapters(text, f"{info.corpus}{grade}")
        for ch in chapters:
            ch.topic_blueprints = split_topic_blueprints(ch.body, ch.title)
            save_chapter(ch, dest, grade)

            records[ch.key] = Record(
                chapter=ch,
                grade=grade,
                subject=info.subject,
                corpus_key=info.corpus,
                blue_key=info.blue,
            )
            print(f"  ✓ {ch.key}: {len(ch.topic_blueprints)} topic_blueprints")

    return records


# ---------------------------------------------------------------------------
# topic_blueprint generation
# ---------------------------------------------------------------------------

def build_topic_blueprint(all_data: Mapping[str, Record]) -> None:
    bp = {
        "project_info": {
            "name": "Physics & Mathematics MCQ Generator",
            "grades": ["11", "12"],
            "subjects": ["Physics", "Mathematics"],
        },
        "structure": {"physics": {}, "mathematics": {}},
    }

    for rec in all_data.values():
        subj = bp["structure"].setdefault(rec.blue_key, {})
        grade = subj.setdefault(f"Grade {rec.grade}", {})

        grade[f"Chapter {rec.chapter.number}"] = {
            "title": rec.chapter.title,
            "chapter_id": rec.chapter.key,
            "topic_blueprints": [
                {"title": t.title, "file": t.rel_path or "", "heading_level": t.level}
                for t in rec.chapter.topic_blueprints
            ],
        }

    (topic_blueprint_DIR / "topic_blueprint.json").write_text(
        json.dumps(bp, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print("topic_blueprint generated")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    setup_dirs()
    src = Path("data_raw")

    configs = (
        SubjectInfo(
            subject="Physics",
            corpus="physics",
            blue="physics",
            files=("Physics_11.md", "Physics_12.md", "PHY 11.md", "PHY 12.md"),
        ),
        SubjectInfo(
            subject="Mathematics",
            corpus="math",
            blue="mathematics",
            files=("Math_11.md", "Math_12.md", "MATH 11.md", "MATH 12.md"),
        ),
    )

    phy_data = run_subject(configs[0], src)
    math_data = run_subject(configs[1], src)

    all_data = {**phy_data, **math_data}
    build_topic_blueprint(all_data)


if __name__ == "__main__":
    main()
