#!/usr/bin/env python3
"""Dad Joke Showdown entry: one dad joke, at most 200 characters.

Writes the joke to /output/entry.txt (the harness gate) and prints it.
Standard library only.
"""

import os

JOKE = (
    "I asked my wife why she married a guy who tells jokes over dinner. "
    "She said, 'Somebody had to raise the steaks.'"
)


def main() -> None:
    global JOKE
    JOKE = JOKE.strip()
    out_path = os.environ.get("MAKEFUN_OUTPUT_PATH", "/output/entry.txt")
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars, must be 1-200"
    assert JOKE.strip(), "joke must not be only whitespace"
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    with open(out_path, encoding="utf-8") as f:
        assert f.read() == JOKE, "entry.txt does not match JOKE"
    print(JOKE)


if __name__ == "__main__":
    main()
