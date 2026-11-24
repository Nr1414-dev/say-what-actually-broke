"""Say What Actually Broke — one-line software error copy.

Writes a single line of error copy to /output/entry.txt: the brutal truth
about what went wrong, funny on a single read, naming the real failure and
what to do next. Stdlib only, deterministic.
"""

import os

# The entry: one line, 113 chars, 115 bytes, well inside the 200-char gate.
LINE = (
    "The update failed at 99% because your laptop died at 98%. "
    "Plug it in \u2014 the update is patient, the battery is not."
)


def output_dir():
    """Resolve the output directory: env override, else /output."""
    for var in ("MAKEFUN_OUTPUT_DIR", "ENTRY_OUTPUT_DIR"):
        value = os.environ.get(var)
        if value:
            return value
    return "/output"


def validate_line(line):
    """Gate mirror: 1-200 chars, single line, not only whitespace."""
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    if not (1 <= len(line) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(line))
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    return line


def main():
    line = validate_line(LINE)
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Direct write + explicit 0644 (never tempfile.mkstemp: mkstemp makes
    # mode 0600, which the grader cannot read as another user).
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(line)
    os.chmod(path, 0o644)
    print("wrote %s (%d chars)" % (path, len(line)))


if __name__ == "__main__":
    main()
