import os

class Solution:
    def __init__(self, input_file_path) -> None:
        self.input_file_path = input_file_path
        self.running_total = 0

    # part 1
    def parse_input(self):
        with open(self.input_file_path, "r") as input_file:

            for line in input_file:
                numbers = [int(x) for x in line.split()]
                self.running_total += max(numbers) - min(numbers)

    def get_running_total(self):
            return self.running_total
                

if __name__ == "__main__":
    input_file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    
    sol = Solution(input_file_path)
    sol.parse_input()
    print(sol.get_running_total())
    
