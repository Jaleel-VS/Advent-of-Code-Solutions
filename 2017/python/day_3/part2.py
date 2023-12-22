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
        self.position = 1
        self.direction = Direction.UP
        self.number_to_find = self.get_number_to_find()
        self.matrix = self.get_matrix()
        self.coordinates = [len(self.matrix) // 2, len(self.matrix) // 2]
        self.matrix[self.coordinates[0]][self.coordinates[1]] = 1
        self.current_sum = self.matrix[self.coordinates[0]][self.coordinates[1]]

    
    def get_coordinates(self):
        return self.coordinates
    
    def update_current_sum(self):
        self.current_sum = self.sum_adjacent(self.coordinates[0], self.coordinates[1])
        print(self.current_sum)
        self.matrix[self.coordinates[0]][self.coordinates[1]] = self.current_sum
    
    
    def sum_adjacent(self, x, y):
        total = 0

        for i in range(-1, 2):
            for j in range(-1, 2):
                if x + i < 0 or y + j < 0:
                    continue
                if x + i >= len(self.matrix) or y + j >= len(self.matrix):

                    continue
                if i == 0 and j == 0:
                    continue

                total += self.matrix[x + i][y + j]

        return total


    def get_matrix(self):
        for i in range(self.number_to_find):
            if i ** 2 > self.number_to_find:
                return [[0 for _ in range(i)] for _ in range(i)]

    def get_number_to_find(self):
        with open(self.input_file_path, "r") as f:
            return int(f.read().strip())

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
            if self.current_sum > self.number_to_find:
                return self.coordinates

            if new_layer:
                self.coordinates[0] += 1
                self.position += 1
                self.update_current_sum()
                new_layer = False
                self.direction = Direction.UP
                continue
            
            self.position += 1
            self.update_coordinates()
            self.update_current_sum()
         

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
        self.coordinates = self.traverse_grid()
        print(self.coordinates)
        print(self.current_sum)




if __name__ == "__main__":
    input_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")
    solution = Solution(input_file_path)

    solution.run()