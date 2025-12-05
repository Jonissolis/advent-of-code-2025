"""Advent of Code base class for daily solutions."""


class AOCDay:
    """Base class for Advent of Code daily challenges."""

    def __init__(self, day, use_test=False, test_name="test.txt"):
        """Initialize the AOC day with input file.

        Args:
            day: The day number as a string.
            use_test: Whether to use test input (default: False).
            test_name: Name of the test file (default: "test.txt").
        """
        self.input_file = (
            f"Day{day}/{test_name}"
            if use_test
            else f"Day{day}/input.txt"
        )
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
    