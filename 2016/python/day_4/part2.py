import os
from part1 import Solution as Part1Solution

class Solution:
    def __init__(self, input_path) -> None:
        self.input_path = input_path
        self.partOneSolution = Part1Solution(input_path)
        self.hidden_sector_id = 0

    def parse_input(self):
        with open(self.input_path) as f:
            for room in f:
                stripped_room = self.partOneSolution.remove_special_characters(room)
                checksum = self.partOneSolution.get_checksum(stripped_room)
                sector_id = self.partOneSolution.get_sector_id(stripped_room)
                room_name = self.partOneSolution.get_room_name(stripped_room)

                if (self.partOneSolution.check_if_real_room(room_name, checksum)):
                    if "northpole" in self.decrypt_room_name(room_name, sector_id):
                        self.hidden_sector_id = sector_id
                        return

    def get_shifted_letter(self, letter, shift):
        if letter == "-":
            return " "
        else:
            return chr(((ord(letter) - 97 + shift) % 26) + 97)
        
    def decrypt_room_name(self, room_name, sector_id):
        return "".join(list(map(lambda x: self.get_shifted_letter(x, sector_id), room_name)))
    
    def get_hidden_sector_id(self):
        return self.hidden_sector_id


if __name__ == "__main__":
    solution = Solution(os.path.join(os.path.dirname(__file__), "input.txt"))

    solution.parse_input()
    print(solution.get_hidden_sector_id())
