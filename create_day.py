"""Create Advent of Code day directory and template files.

Usage (recommended):
  python create_day.py 3
  python create_day.py 3 --target "c:/path/to/2025"
  python create_day.py --from-cwd        # run inside an existing DayN folder
  python create_day.py 3 --force         # overwrite existing files
"""

import argparse
import os
import re
import sys
from typing import Optional

MAIN_TEMPLATE = """
import os
from typing import Optional
from aoc_base import AOCDay

class Main(AOCDay):
    def __init__(self, use_test=False, day: Optional[str] = None):
        # If day not provided, auto-detect from current directory name (e.g. "Day1")
        if day is None:
            base = os.path.basename(os.getcwd())
            if base.startswith("Day"):
                day = base.replace("Day", "")
            else:
                error_msg = "Cannot detect day from directory name; provide 'day' explicitly."
                raise RuntimeError(error_msg)
        super().__init__(day=str(day), use_test=use_test)

    def part_one(self):
        raise NotImplementedError

    def part_two(self):
        raise NotImplementedError


def main():
    program = Main(use_test=True)
    print(f'Part 1 answer: {program.part_one()}')
    print(f'Part 2 answer: {program.part_two()}')


if __name__ == "__main__":
    main()
"""


def validate_day_int(day) -> int:
    """Validate that `day` is an integer between 1 and 25 and return it."""
    try:
        value = int(day)
    except (TypeError, ValueError) as exc:
        raise argparse.ArgumentTypeError("day must be an integer between 1 and 25") from exc
    if not 1 <= value <= 25:
        raise argparse.ArgumentTypeError("day must be between 1 and 25")
    return value


def detect_day_from_cwd() -> Optional[int]:
    """Return the day number detected from the current directory name, or None."""
    base = os.path.basename(os.getcwd())
    m = re.fullmatch(r"[Dd]ay(\d{1,2})", base)
    if m:
        return int(m.group(1))
    return None


def write_file(path: str, content: str, force: bool) -> None:
    """Write `content` to `path`. Skip if file exists and `force` is False."""
    if os.path.exists(path) and not force:
        print(f"Skipping existing {path} (use --force to overwrite)")
        return
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Wrote {path}")


def create_day(day: int, target_dir: str, force: bool) -> None:
    """Create `Day{day}` under `target_dir` with a test.txt and main.py template."""
    day_dir = os.path.join(target_dir, f"Day{day}")
    os.makedirs(day_dir, exist_ok=True)

    # test.txt (empty)
    test_path = os.path.join(day_dir, "test.txt")
    write_file(test_path, "", force)

    # main.py (template)
    main_py_path = os.path.join(day_dir, "main.py")
    write_file(main_py_path, MAIN_TEMPLATE, force)

    print(f"Created/updated day folder: {day_dir}")


def populate_cwd(force: bool) -> None:
    """Populate the current `DayN` folder with `main.py` and `test.txt` (auto-detects day)."""
    detected = detect_day_from_cwd()
    if detected is None:
        print("Current directory is not named like 'DayN' (e.g. 'Day3'). Aborting.")
        sys.exit(1)
    target_dir = os.getcwd()
    # Write files directly into cwd (respecting --force)
    write_file(os.path.join(target_dir, "test.txt"), "", force)
    write_file(os.path.join(target_dir, "main.py"), MAIN_TEMPLATE, force)
    print("Populated current Day folder.")


def parse_args(argv):
    """Parse CLI arguments and return the parsed namespace."""
    parser = argparse.ArgumentParser(description="Create Advent of Code day template")
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--from-cwd",
        action="store_true",
        help="Populate the current DayN folder (auto-detect day)",
    )
    group.add_argument(
        "--target",
        type=str,
        help="Target directory (year folder). Defaults to current working directory.",
    )
    parser.add_argument(
        "day",
        nargs="?",
        type=validate_day_int,
        help="Day number (1-25). Not required when --from-cwd is used.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing files",
    )
    return parser.parse_args(argv)


def main(argv):
    """Entry point: handle args and call the appropriate creation/population function."""
    args = parse_args(argv)

    if args.from_cwd:
        populate_cwd(force=args.force)
        return

    if args.day is None:
        print("Either provide a day number or use --from-cwd to populate the current DayN folder.")
        sys.exit(1)

    target = args.target if args.target is not None else os.getcwd()
    target = os.path.abspath(target)

    if not os.path.isdir(target):
        print(f"Target directory does not exist: {target}")
        sys.exit(1)

    create_day(args.day, target, force=args.force)


if __name__ == "__main__":
    main(sys.argv[1:])
