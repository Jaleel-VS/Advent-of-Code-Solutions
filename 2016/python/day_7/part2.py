import os
import part1

class Solution:
    def __init__(self, input_file_path) -> None:
        self.input_file_path = input_file_path

        self.part1_solution = part1.Solution(self.input_file_path)
        self.supports_ssl = 0

    def get_babs(self, segment):
        babs = []
        for i in range(len(segment) - 2):
            if segment[i] == segment[i + 2] and segment[i] != segment[i + 1]:
                babs.append(segment[i:i + 3])

        return babs
    
    def get_aba(self, bab):
        return bab[1] + bab[0] + bab[1]
    
    def is_ssl(self, ip):
        inside_brackets, outside_brackets = self.part1_solution.get_segments(ip)
        
        for segment in inside_brackets:
            babs = self.get_babs(segment)
            for bab in babs:
                aba = self.get_aba(bab)
                for segment in outside_brackets:
                    if aba in segment:
                        return True
                    
        return False
            
    def get_supports_ssl(self):
        with open(self.input_file_path) as input_file:
            for ip in input_file:
                if self.is_ssl(ip.strip()):
                    self.supports_ssl += 1

        return self.supports_ssl
    
if __name__ == "__main__":
    solution = Solution(os.path.join(os.path.dirname(__file__), "input.txt"))

    print(solution.get_supports_ssl())
    