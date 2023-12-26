# part 1 involves summing up all the numbers in the input file
import os

class Solution:
    def __init__(self, input_file_path):
        self.input_file_path = input_file_path

        self.run()

    def run(self):
        with open(self.input_file_path) as f:
            lines = f.readlines()

        lines = [line.strip() for line in lines]
        
        total = 0

        for line in lines:
            sign, value = line[0], line[1:]

            total += int(value) if sign == "+" else -int(value)

        print(total)

            


if __name__ == "__main__":
    input_file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    solution = Solution(input_file_path)