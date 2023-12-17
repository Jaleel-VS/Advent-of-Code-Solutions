import os
import hashlib

class Solution:
    def __init__(self, input_path) -> None:
        self.input_path = input_path

    def get_id_from_input(self):
        with open(self.input_path) as f:
            return f.read().strip()
        
    def get_password(self):
        i = 0
        password = ""
        door_id = self.get_id_from_input()

        while len(password) < 8:
            md5_hash = hashlib.md5(f"{door_id}{i}".encode()).hexdigest()

            if md5_hash.startswith("00000"):
                password += md5_hash[5]

            i += 1
        
        return password
            

if __name__ == "__main__":
    input_path = os.path.join(os.path.dirname(__file__), "input.txt")

    solution = Solution(input_path)
    print(solution.get_password())