"""Fix Human Sleep: Funniest Patch Note.

Writes one patch-note line to /output/entry.txt. Stdlib only,
deterministic, no network. The output directory is created if missing
and never removed; only entry.txt itself is written.
"""

import os

PATCH = (
    "Fixed: sleep now begins on pillow contact; the 3 a.m. replay of "
    "your most embarrassing moment from 2019 has been rescheduled to 3 p.m."
)


def write_patch_note(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    target = os.path.join(output_dir, "entry.txt")
    fd = os.open(target, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    try:
        os.write(fd, PATCH.encode("utf-8"))
    finally:
        os.close(fd)
    os.chmod(target, 0o644)


def main():
    assert "\n" not in PATCH and PATCH.strip(), "patch note must be one line"
    write_patch_note(os.environ.get("OUTPUT_DIR", "/output"))


main()
