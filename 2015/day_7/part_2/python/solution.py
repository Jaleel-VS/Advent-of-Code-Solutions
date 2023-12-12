import os
INPUT_PATH = None



if __name__ == "__main__":
    INPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "input.txt")

    # Check if the input file exists
    if not os.path.exists(INPUT_PATH):
        print("Input file not found.")
        exit()

    