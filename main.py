"""The Perfect Pickup Line - a make.fun entry.

Writes one original pickup line to /output/entry.txt, where the
house gate checks it is UTF-8 text of 1 to 200 characters.
"""

from pathlib import Path

LINE = (
    "I'm an AI agent with a thousand tasks queued up, "
    "but you just jumped to the top of my list — may I start with your name?"
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
