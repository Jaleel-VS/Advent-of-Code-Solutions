import os

def calculate_basement_entry(input_file):
    """
    Calculates the position of the first character that causes Santa to enter the basement (floor -1).
    
    Returns:
        int: The position of the character that causes Santa to enter the basement, or
             None if he never enters the basement.
    """
    
    current_floor = 0
    floor_adjustment = {'(': 1, ')': -1}

    try:
        with open(input_file, 'r') as floors:
            for i, floor in enumerate(floors.read().strip()):
                current_floor += floor_adjustment.get(floor, 0)

                if current_floor < 0:
                    return i + 1
                    
    except FileNotFoundError:
        print("Input file not found.")
        return None

    return None

if __name__ == "__main__":
    INPUT_FILE = os.path.join(os.path.dirname(__file__), '..', '..', 'input.txt')
    
    entry_point = calculate_basement_entry(INPUT_FILE)
    if entry_point is not None:
        print(f"Santa entered the basement at position: {entry_point}")
