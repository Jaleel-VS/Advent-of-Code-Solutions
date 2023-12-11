import os
INPUT_PATH = None

def get_houses_visited(input_file):
    x, y = 0, 0
    houses = set()
    houses.add((x, y))

    with open(input_file, "r") as f:
        directions = f.read()

    for direction in directions:
        if direction == "^":
            y += 1
        elif direction == "v":
            y -= 1
        elif direction == ">":
            x += 1
        elif direction == "<":
            x -= 1

        houses.add((x, y))

    return houses

if __name__ == "__main__":
    INPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "input.txt")

    # Check if the input file exists
    if not os.path.exists(INPUT_PATH):
        print("Input file not found.")
        exit()

    houses = get_houses_visited(INPUT_PATH)

    print(f"Santa visited {len(houses)} houses.")
    
    