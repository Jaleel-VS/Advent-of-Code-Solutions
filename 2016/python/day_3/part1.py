import os

class Solution:
    def __init__(self, input_path) -> None:
        self.input_path = input_path
        self.valid_triangles = 0

    def count_valid_triangles(self):
        with open(self.input_path) as f:
            for line in f:
                triangle = [int(x) for x in line.split()]
                if self.is_valid_triangle(triangle):
                    self.valid_triangles += 1

    def is_valid_triangle(self, triangle):
        return triangle[0] + triangle[1] > triangle[2] and triangle[0] + triangle[2] > triangle[1] and triangle[1] + triangle[2] > triangle[0]
    
    def get_valid_triangles(self):
        return self.valid_triangles

if __name__ == '__main__':
    input_file_path = os.path.join(os.path.dirname(__file__), "input.txt")

    solution = Solution(input_file_path)
    solution.count_valid_triangles()
    print(f"""The number of valid triangles is {solution.get_valid_triangles()}""")
    