Day = "X"
class Main:
    def __init__(self, use_test = False):
        if use_test:
            self.input_file = "Day" + Day + "/test.txt"
        else:
            self.input_file = "Day" + Day + "/input.txt"
        self.interpret_file()

    def interpret_file(self):
        with open(self.input_file, "r") as f:
            input_string = f.read()
    
    def part_one(self):
        return NotImplemented
    def part_two(self):
        return NotImplemented


def main():
    program = Main(use_test=True)
    print(f'Part 1 answer: {program.part_one()}')
    print(f'Part 2 answer: {program.part_two()}')


if __name__ == "__main__":
    main()