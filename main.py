"""Write the entry sentence for make.fun's "The Best Meal You Ever Had".

Pure standard library. Deterministic: the same sentence is written on
every run. The program enforces the competition gate itself -- the file
must hold 1 to 200 characters including its single trailing newline --
and refuses to write anything that would fail it.
"""

import os
import sys

SENTENCE = "The hospital vending-machine turkey sandwich, stale bread and cold tomato, was the best meal I ever had, its wrapper crinkling louder than the monitor's beep as I waited for the surgeon's thumbs-up."

# Gate: entry.txt is UTF-8 text of 1 to 200 characters, not only whitespace.
MAX_CHARS = 200


def build_entry() -> str:
    """Return the exact file contents: the sentence plus one newline."""
    text = SENTENCE + "\n"
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry would be %d characters, outside the 1-%d gate"
            % (len(text), MAX_CHARS)
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main() -> None:
    try:
        text = build_entry()
    except ValueError as exc:
        print("error: %s" % exc, file=sys.stderr)
        raise SystemExit(1)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
