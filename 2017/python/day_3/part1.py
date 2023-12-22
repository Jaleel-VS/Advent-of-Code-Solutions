import os
import enum

class Direction(enum.Enum):
    RIGHT = 0
    UP = 1
    LEFT = 2
    DOWN = 3

class Solution:
    def __init__(self, input_file_path):
        self.input_file_path = input_file_path
        self.coordinates = [0, 0]
        self.direction = Direction.UP
        self.position = 1
        self.number_to_find = -1



    def read_input(self):
        with open(self.input_file_path, "r") as f:
            self.number_to_find = int(f.read().strip())

    def get_corners(self, row):
        corners = []

        for i in range(4):
            corners.append(row ** 2 - (row - 1) * i)

        corners.sort()
        return corners

    def traverse_grid(self):
        layer = 3

        new_layer = True

        corners = self.get_corners(layer)

        while True:
            if self.position == self.number_to_find:
                return self.coordinates

            if new_layer:
                self.coordinates[0] += 1
                self.position += 1
                new_layer = False
                self.direction = Direction.UP
                continue
            
            self.position += 1
            self.update_coordinates()

            if self.position == corners[0]:
                self.direction = Direction.LEFT
            elif self.position == corners[1]:
                self.direction = Direction.DOWN
            elif self.position == corners[2]:
                self.direction = Direction.RIGHT
            elif self.position == corners[3]:
                self.direction = Direction.RIGHT
                new_layer = True
                layer += 2
                corners = self.get_corners(layer)



    def update_coordinates(self):
        if self.direction == Direction.RIGHT:
            self.coordinates[0] += 1
        if self.direction == Direction.UP:
            self.coordinates[1] += 1
        if self.direction == Direction.LEFT:
            self.coordinates[0] -= 1
        if self.direction == Direction.DOWN:
            self.coordinates[1] -= 1

    def run(self):
        self.read_input()
        self.coordinates = self.traverse_grid()
        print(self.coordinates)
        print(sum(map(abs, self.coordinates)))




if __name__ == "__main__":
    input_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")
    solution = Solution(input_file_path)

    solution.run()