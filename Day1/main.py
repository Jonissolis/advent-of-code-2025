"""Day solution template.

This template always auto-detects the day from the current directory name
(e.g. 'Day3'). It does not require editing the file to set the day.
"""

import os
import numpy as np

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
        dial_num = 50
        zeroes = 0
        for line in self.input_string.splitlines():
            direction = line[0]
            amount = int(line[1:])
            dial_num += (amount if direction == 'R' else -amount)
            dial_num %= 100
            if dial_num == 0:
                zeroes += 1
        return zeroes

    def part_two(self):
        dial_num = 50
        zeroes = 0
        for line in self.input_string.splitlines():
            direction = line[0]
            amount = int(line[1:])
            if amount > 100:
                zeroes += amount // 100
                amount %= 100
            prev_dial_num  = dial_num
            dial_num += (amount if direction == 'R' else -amount)
            if np.sign(prev_dial_num)*np.sign(dial_num) == -1 or \
                np.sign(prev_dial_num-100)*np.sign(dial_num-100) == -1:
                zeroes += 1
            if dial_num == 0 or dial_num == 100:
                zeroes += 1
            dial_num %= 100

        return zeroes


def main():
    program = Main(use_test=True)
    print(f"Part 1 answer: {program.part_one()}")
    print(f"Part 2 answer: {program.part_two()}")


if __name__ == "__main__":
    main()
