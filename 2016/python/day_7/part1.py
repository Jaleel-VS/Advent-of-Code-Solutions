import os

class Solution:
    def __init__(self, input_file_path) -> None:
        self.input_file_path = input_file_path
        self.supports_tls = 0

    def get_segments(self, ip):
        inside_brackets = []
        outside_brackets = []
        temp_string = ""
        i = 0
        inside = False
        
        while i < len(ip):
            if ip[i] == "[":
                if temp_string != "": outside_brackets.append(temp_string)
                temp_string = ""
                inside = True
                i += 1
                while ip[i] != "]":
                    temp_string += ip[i]
                    i += 1

                inside_brackets.append(temp_string)
                temp_string = ""
                inside = False
                
            else:
                temp_string += ip[i]
            i += 1

        if temp_string:
            if inside:
                inside_brackets.append(temp_string)
            else:
                outside_brackets.append(temp_string)

        return inside_brackets, outside_brackets
    
    def is_abba(self, segment):
        for i in range(len(segment) - 3):
            if segment[i] == segment[i + 3] and segment[i + 1] == segment[i + 2] and segment[i] != segment[i + 1]:
                return True

        return False
    
    def is_tls(self, ip):
        inside_brackets, outside_brackets = self.get_segments(ip)

        for segment in inside_brackets:
            if self.is_abba(segment):
                return False
            
        for segment in outside_brackets:
            if self.is_abba(segment):
                return True
            
        return False
    
    def get_supports_tls(self):
        with open(self.input_file_path, "r") as input_file:
            for line in input_file:
                if self.is_tls(line.strip()):
                    self.supports_tls += 1
        
        return self.supports_tls


if __name__ == "__main__":
    input_file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    
    sol = Solution(input_file_path)

    print(sol.get_supports_tls())