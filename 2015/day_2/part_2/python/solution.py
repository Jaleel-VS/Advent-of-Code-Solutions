import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), '..', '..', 'input.txt')

def smallest_perimeter(l, w, h):
    return min(2 * (l + w), 2 * (w + h), 2 * (h + l))

def bow_length(l, w, h):
    return l * w * h

def calculate_ribbon_length(input_file):
    total_length = 0
    with open(input_file) as file:
        for line in file:
            l, w, h = sorted([int(x) for x in line.split('x')])
            total_length += smallest_perimeter(l, w, h) + bow_length(l, w, h)

    return total_length

if __name__ == '__main__':
    print(f'The total length of ribbon required is {calculate_ribbon_length(INPUT_FILE)}')