import os

class Solution:
    def __init__(self, input_file_path) -> None:
        self.input_file_path = input_file_path
        self.running_total = 0

    def parse_input(self):
        with open(self.input_file_path, "r") as input_file:
            digits = input_file.read().strip()
            for i in range(len(digits)):
                if digits[i] == digits[(i + 1) % len(digits)]:
                    self.running_total += int(digits[i])

    def get_running_total(self):
        return self.running_total
                


if __name__ == "__main__":
    input_file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    
    sol = Solution(input_file_path)
    sol.parse_input()
    print(sol.get_running_total())