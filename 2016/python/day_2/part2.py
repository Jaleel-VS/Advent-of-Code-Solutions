import os

class Solution:
    def __init__(self, input_file_path) -> None:
        self.input_file_path = input_file_path
        self.key_pad = [[0, 0, 1, 0, 0], 
                        [0, 2, 3, 4, 0], 
                        [5, 6, 7, 8, 9], 
                        [0, 'A', 'B', 'C', 0], 
                        [0, 0, 'D', 0, 0]]
        self.current_position  = [2, 0]
        self.code = []

    def process_code(self):
        with open(self.input_file_path, "r") as f:
            for line in f:
                for direction in line:
                    new_x, new_y = self.current_position[0], self.current_position[1]
                    if direction == 'U':
                        new_x = max(0, self.current_position[0] - 1)
                        if self.key_pad[new_x][new_y] != 0:
                            self.current_position[0] = new_x
                    elif direction == 'D':
                        new_x = min(len(self.key_pad) - 1, self.current_position[0] + 1)
                        if self.key_pad[new_x][new_y] != 0:
                            self.current_position[0] = new_x
                    elif direction == 'L':
                        new_y = max(0, self.current_position[1] - 1)
                        if self.key_pad[new_x][new_y] != 0:
                            self.current_position[1] = new_y
                    elif direction == 'R':
                        new_y = min(len(self.key_pad[0]) - 1, self.current_position[1] + 1)
                        if self.key_pad[new_x][new_y] != 0:
                            self.current_position[1] = new_y
                        
                self.update_code(self.current_position[0], self.current_position[1])
    
    def update_code(self, x, y):
        self.code.append(self.key_pad[x][y])
    
    def get_code(self):
        return ''.join(str(x) for x in self.code)

                            


if __name__ == "__main__":
    input_file_path = os.path.join(os.path.dirname(__file__), "input.txt")

    solution = Solution(input_file_path)
    solution.process_code()
    print(f"""The code is: {solution.get_code()}""")