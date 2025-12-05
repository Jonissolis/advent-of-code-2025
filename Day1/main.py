
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
