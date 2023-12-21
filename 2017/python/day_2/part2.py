import os

class Solution:
    def __init__(self, input_file_path) -> None:
        self.input_file_path = input_file_path
        self.running_total = 0

    # part 2
    def parse_input(self):
        with open(self.input_file_path, "r") as input_file:

            for line in input_file:
                numbers = [int(x) for x in line.split()]
                for i in range(len(numbers)):
                    for j in range(len(numbers)):
                        if i != j and numbers[i] % numbers[j] == 0:
                            self.running_total += numbers[i] // numbers[j]
                            break

    def get_running_total(self):
            return self.running_total
                

if __name__ == "__main__":
    input_file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    
    sol = Solution(input_file_path)
    sol.parse_input()
    print(sol.get_running_total())
    
