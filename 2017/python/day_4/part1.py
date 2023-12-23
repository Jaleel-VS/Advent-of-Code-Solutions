import os

class Solution(object):
    def __init__(self, input):
        self.input = input

    def solve(self):
        valid = 0
        for line in self.input:
            words = line.split()
            if len(words) == len(set(words)):
                valid += 1
        return valid
    
if __name__ == '__main__':
    input = open(os.path.join(os.path.dirname(__file__), 'input.txt')).readlines()
    print(Solution(input).solve())