import os
import hashlib

class Solution:
    def __init__(self, input_file_path) -> None:
        self.input_file_path = input_file_path
        self.password = [" "] * 8

    def get_id_from_input(self):
        with open(self.input_file_path, "r") as input_file:
            return input_file.read().strip()

    def get_password(self):
        i = 0
        door_id = self.get_id_from_input()

        while True:
            md5_hash = hashlib.md5(f"{door_id}{i}".encode()).hexdigest()

            if md5_hash.startswith("00000"):
                hidden_index = md5_hash[5]
                hidden_value = md5_hash[6]

                if hidden_index.isdigit() and int(hidden_index) < 8 and self.password[int(hidden_index)] == " ":
                    self.password[int(hidden_index)] = hidden_value

                    if " " not in self.password:
                        return "".join(self.password)

            i += 1
        
        return password
    
if __name__ == "__main__":
    password = Solution(os.path.join(os.path.dirname(__file__), "input.txt")).get_password()

    print(password)