import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), '..', '..', 'input.txt')

def get_surface_area(l, w, h):
    return 2*l*w + 2*w*h + 2*h*l

def get_smallest_side_area(l, w, h):
    return min(l*w, w*h, h*l)

def calculate_wrapping_paper(input_file):
    """
    Calculate the total amount of wrapping paper needed based on the dimensions
    of the presents specified in the input file.

    Args:
        input_file (str): Path to the input file containing the dimensions of the presents.

    Returns:
        int: The total amount of wrapping paper needed in square units.
    """

    total_wrapping_paper = 0

    try:
        with open(input_file, 'r') as presents:
            for present in presents:
                l, w, h = [int(x) for x in present.strip().split('x')]
                total_wrapping_paper += get_surface_area(l, w, h) + get_smallest_side_area(l, w, h)
    except FileNotFoundError:
        print("Input file not found.")
        return None

    return total_wrapping_paper

if __name__ == "__main__":
    total_wrapping_paper = calculate_wrapping_paper(INPUT_FILE)
    if total_wrapping_paper is not None:
        print(f"Total wrapping paper needed: {total_wrapping_paper} square units")
