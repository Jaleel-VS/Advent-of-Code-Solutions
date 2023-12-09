import os

def calculate_final_floor(input_file):
    """
    Calculates the final floor based on the instructions in the input file.
    An opening parenthesis '(' means go up one floor,
    and a closing parenthesis ')' means go down one floor.
    """
    current_floor = 0
    floor_adjustment = {'(': 1, ')': -1}

    try:
        with open(input_file, 'r') as floors:
            for floor in floors.read().strip():
                current_floor += floor_adjustment.get(floor, 0)
    except FileNotFoundError:
        print("Input file not found.")
        return None

    return current_floor

if __name__ == "__main__":
    INPUT_FILE = os.path.join(os.path.dirname(__file__), '..', '..', 'input.txt')
    
    final_floor = calculate_final_floor(INPUT_FILE)
    if final_floor is not None:
        print(f"Santa has reached floor: {final_floor}")
