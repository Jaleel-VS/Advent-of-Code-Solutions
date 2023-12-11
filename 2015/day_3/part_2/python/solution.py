import os
INPUT_PATH = None

def get_houses_visited(directions):
    x, y, x1, y1 = 0, 0, 0, 0

    houses = set()
    houses.add((x, y))

    for i, direction in enumerate(directions):
        if i % 2 == 0:
            if direction == "^":
                y += 1
            elif direction == "v":
                y -= 1
            elif direction == ">":
                x += 1
            elif direction == "<":
                x -= 1
            houses.add((x, y))
        else:
            if direction == "^":
                y1 += 1
            elif direction == "v":
                y1 -= 1
            elif direction == ">":
                x1 += 1
            elif direction == "<":
                x1 -= 1
            houses.add((x1, y1))

    return len(houses)


if __name__ == "__main__":
    INPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "input.txt")

    # Check if the input file exists
    if not os.path.exists(INPUT_PATH):
        print("Input file not found.")
        exit()
    
    with open(INPUT_PATH) as f:
        directions = f.read().strip()

    print(get_houses_visited(directions))

    