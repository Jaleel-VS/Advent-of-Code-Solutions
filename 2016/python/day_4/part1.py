import os

class Solution:
    def __init__(self, input_path) -> None:
        self.input_path = input_path
        self.sum_of_sector_ids = 0

    def parse_input(self):
        with open(self.input_path) as f:
            for room in f:
                stripped_room = self.remove_special_characters(room)
                checksum = self.get_checksum(stripped_room)
                sector_id = self.get_sector_id(stripped_room)
                room_name = self.get_room_name(stripped_room)

                if (self.check_if_real_room(room_name, checksum)):
                    self.sum_of_sector_ids += sector_id


    def remove_special_characters(self, room):
        return room.replace("-", "").replace("[", "").replace("]", "").replace("\n", "")
    
    def get_checksum(self, room):
        return room[-5:]
    
    def get_sector_id(self, room):
        return int(room[-8:-5])
    
    def get_room_name(self, room):
        return room[:-8]
    
    def check_if_real_room(self, room_name, checksum):
        self.letter_count = {}

        for letter in room_name:
            if letter in self.letter_count:
                self.letter_count[letter] += 1
            else:
                self.letter_count[letter] = 1

        sorted_letter_count = sorted(self.letter_count.items(), key=lambda x: (-x[1], x[0]))

        for i in range(5):
            if sorted_letter_count[i][0] != checksum[i]:
                return False
        
        return True
    

    def get_sum_of_sector_ids(self):
        return self.sum_of_sector_ids
    

if __name__ == "__main__":
    solution = Solution(os.path.join(os.path.dirname(__file__), "input.txt"))
    solution.parse_input()
    print(solution.get_sum_of_sector_ids())
    




    
    
    