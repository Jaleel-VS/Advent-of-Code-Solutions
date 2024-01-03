import os
import requests

class Solution:
    def __init__(self, input_file_path):
        self.input_file_path = input_file_path
    
    def solve(self, ):
        max_calories = float('-inf')
        calories_count = 0
        with open(self.input_file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line.isdigit():
                    calories_count += int(line)
                
                else:
                    max_calories = max(max_calories, calories_count)
                    calories_count = 0

            max_calories = max(max_calories, calories_count)
    
        print(max_calories)
                


if __name__ == "__main__":
    input_file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    Solution(input_file_path).solve()
