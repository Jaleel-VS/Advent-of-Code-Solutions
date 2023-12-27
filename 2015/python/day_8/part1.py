import os
import re

class Solution:
    def __init__(self, input_file_path):
        self.input_file_path = input_file_path
        self.total = 0

        self.run()

    
    def run(self):
        with open(self.input_file_path) as strings:
            for string in strings:
                raw_string_length = self.get_raw_string_len(string)
                in_memory_string_length = self.get_in_memory_string_len(string)

                print(f"raw: {raw_string_length}, in memory: {in_memory_string_length}")

                self.total += raw_string_length - in_memory_string_length

        print(self.total)
                
    
    def get_raw_string_len(self, string: str):
        return len(string.strip())
    
    def get_in_memory_string_len(self, string):
        # remove newline and whitespace
        string = string.strip()

        # remove quotes
        string = string[1:-1]

        # remove escaped quotes
        string = string.replace("\\\"", "\"")

        # remove escaped backslashes
        string = string.replace("\\\\", "\\")

        # remove escaped hex
        string = re.sub(r"\\x[0-9a-f]{2}", "_", string)

        return len(string)






if __name__ == "__main__":
    input_file_path = os.path.join(os.path.dirname(__file__), "input.txt")

    solution = Solution(input_file_path)