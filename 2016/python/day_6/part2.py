import os

class Solution:
    def __init__(self, input_file_path) -> None:
        self.input_file_path = input_file_path
        self.word_2d_array = []
        self.secret_word = ""
    

    def parse_input(self):
        with open(self.input_file_path, "r") as input_file:
            for line in input_file:
                self.word_2d_array.append(list(line.strip()))

    def get_least_common_letter(self):

        for i in range(len(self.word_2d_array[0])):
            letter_count = {}
            for j in range(len(self.word_2d_array)):
                letter = self.word_2d_array[j][i]
                if letter in letter_count:
                    letter_count[letter] += 1
                else:
                    letter_count[letter] = 1
            
            self.secret_word += min(letter_count, key=letter_count.get)

    def get_secret_word(self):
        return self.secret_word

            

if __name__ == "__main__":
    input_file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    
    sol = Solution(input_file_path)
    sol.parse_input()
    sol.get_least_common_letter()
    print(sol.get_secret_word())