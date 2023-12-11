import os
import hashlib

INPUT_PATH = None

def get_valid_suffix(secret_key):
    start = 1
    while True:
        md5_hash = hashlib.md5(f"{secret_key}{start}".encode()).hexdigest()
        if md5_hash.startswith("000000"):
            return start
        start += 1


if __name__ == "__main__":
    INPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "input.txt")

    # Check if the input file exists
    if not os.path.exists(INPUT_PATH):
        print("Input file not found.")
        exit()

    # Read the input file
    with open(INPUT_PATH, "r") as input_file:
        secret_key = input_file.read().strip()

    # Get the valid hash
    valid_hash = get_valid_suffix(secret_key)
    print(f"The valid hash is: {valid_hash}")

    