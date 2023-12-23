import os

class Solution(object):
    def __init__(self, input):
        self.input = input

    def solve(self):
        valid = 0
        for word in self.input:
            words = word.split()

            invalid_passphrase = False
            for i in range(len(words)):
                for j in range(len(words)):
                    if i != j and len(words[i]) == len(words[j]):
                        if self.is_anagram(words[i], words[j]):
                            invalid_passphrase = True
                            break
                if invalid_passphrase:
                    break
            
            if not invalid_passphrase:
                valid += 1
            

        return valid
    
    def is_anagram(self, word1, word2):
        return sorted(word1) == sorted(word2)
    
if __name__ == '__main__':
    input = open(os.path.join(os.path.dirname(__file__), 'input.txt')).readlines()
    print(Solution(input).solve())