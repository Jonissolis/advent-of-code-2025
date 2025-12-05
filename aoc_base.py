"""Advent of Code base class for daily solutions."""

import os


class AOCDay:
    """Base class for Advent of Code daily challenges."""

    def __init__(self, day, use_test=False, test_name="test.txt"):
        """Initialize the AOC day with input file.

        Args:
            day: The day number as a string.
            use_test: Whether to use test input (default: False).
            test_name: Name of the test file (default: "test.txt").
        """
        # Construct paths relative to this file's location (the 2025/ folder)
        base_dir = os.path.dirname(os.path.abspath(__file__))
        filename = test_name if use_test else "input.txt"
        self.input_file = os.path.join(base_dir, f"Day{day}", filename)
        self.interpret_file()

    def interpret_file(self):
        """Read and store the input file contents."""
        with open(self.input_file, "r", encoding="utf-8") as f:
            self.input_string = f.read()

    def part_one(self):
        """Solve part one of the challenge."""
        raise NotImplementedError

    def part_two(self):
        """Solve part two of the challenge."""
        raise NotImplementedError
