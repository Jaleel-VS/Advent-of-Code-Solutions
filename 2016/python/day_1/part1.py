import os

class Solution:
    def __init__(self, input_file_path) -> None:
        self.input_file_path = input_file_path
        self.x = 0
        self.y = 0
        self.compass = ['N', 'E', 'S', 'W']
        self.current_direction = 'N'

    def get_new_direction(self, direction):
        if direction[0] == 'R':
            index = (self.compass.index(self.current_direction) + 1) % 4
            return self.compass[index]
        elif direction[0] == 'L':
            index = (self.compass.index(self.current_direction) - 1) % 4
            return self.compass[index]
        else:
            print("Unknown direction: {}".format(direction[0]))
            exit()

    def process_direction(self, direction):
        distance = int(direction[1:])
        self.current_direction = self.get_new_direction(direction)

        if self.current_direction == 'N':
            self.y += distance
        elif self.current_direction == 'S':
            self.y -= distance
        elif self.current_direction == 'E':
            self.x += distance
        elif self.current_direction == 'W':
            self.x -= distance

    def calculate_distance(self):
        try:
            with open(self.input_file_path, "r") as f:
                lines = f.read()
                directions = lines.split(", ")

            for direction in directions:
                self.process_direction(direction)

            return abs(self.x) + abs(self.y)
        except IOError:
            print("Error reading file: {}".format(self.input_file_path))
            exit()

if __name__ == "__main__":
    input_file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    solution = Solution(input_file_path)
    print(solution.calculate_distance())
