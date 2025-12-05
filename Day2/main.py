"""Day solution template.

This template always auto-detects the day from the current directory name
(e.g. 'Day3'). It does not require editing the file to set the day.

Run the file by 'python -m DayN.main' from the year folder.
"""

import os

from aoc_base import AOCDay


class Main(AOCDay):
    def __init__(self, use_test: bool = False):
        # Auto-detect the day from the current directory name (e.g. "Day1")
        base = os.path.basename(os.path.dirname(os.path.abspath(__file__)))
        if base.lower().startswith("day"):
            day = base[3:]  # remove the "Day" prefix
        else:
            error_msg = "Cannot detect day from directory name; run from a 'DayN' folder."
            raise RuntimeError(error_msg)
        super().__init__(day=str(day), use_test=use_test)

    def part_one(self):
        raise NotImplementedError

    def part_two(self):
        raise NotImplementedError


def main():
    program = Main(use_test=True)
    try:
        print(f"Part 1 answer: {program.part_one()}")
    except NotImplementedError:
        print("Part 1 not implemented yet.")
    try:
        print(f"Part 2 answer: {program.part_two()}")
    except NotImplementedError:
        print("Part 2 not implemented yet.")


if __name__ == "__main__":
    main()
