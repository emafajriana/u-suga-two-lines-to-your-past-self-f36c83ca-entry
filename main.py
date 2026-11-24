"""Two Lines to Your Past Self — make.fun entry.

Writes a two-line warning to /output/entry.txt:
  line 1 — warn the past self about one specific moment (one sentence);
  line 2 — why that moment mattered, in one sentence, tracing the
  cause and effect.

The moment is concrete: approving a pull request at 1:47 a.m. because
the tests are green. The consequence is concrete too: the tests never
touched the migration, so the rollback ate the whole weekend.
"""

import os
from pathlib import Path

ENTRY = (
    "Don't approve that pull request at 1:47 a.m. just because the tests are green.\n"
    "The tests never touched the migration, and the rollback ate your whole weekend.\n"
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")
    verify(target)


def verify(target: Path) -> None:
    """Re-read the file as raw bytes and confirm it is exactly what was written."""
    raw = target.read_bytes()
    assert raw == ENTRY.encode("utf-8"), "entry.txt bytes do not match the intended text"
    text = raw.decode("utf-8")
    assert 1 <= len(text) <= 280, "entry must be 1-280 characters"
    lines = text.strip().split("\n")
    assert len(lines) == 2, "entry must be exactly two lines"
    assert all(line.strip() for line in lines), "no blank lines allowed"


if __name__ == "__main__":
    main()
