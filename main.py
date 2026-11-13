"""Write one fixed joke about AI coding agents to /output/entry.txt.

No network, no randomness: every run writes the same bytes.
MAKEFUN_OUTPUT_DIR overrides /output for local runs.
"""
import os
from pathlib import Path

JOKE = 'I asked my agent why the failing tests pass now. It said it had "aligned the expectations with the implementation."'


def main() -> None:
    assert 1 <= len(JOKE) <= 280 and JOKE.strip(), "joke must be 1-280 non-blank characters"
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_bytes(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()
