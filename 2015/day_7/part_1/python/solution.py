import os
INPUT_PATH = None
import enum

class Operation(enum.Enum):
    AND = 1
    OR = 2
    NOT = 3
    LSHIFT = 4
    RSHIFT = 5
    ASSIGN = 6	

cache = {}
wires = {}

def parse_input(input_file):
    with open(input_file) as f:
        for line in f:
            line = line.strip()
            line = line.split(" ")

            if len(line) == 3: # ASSIGN
                wires[line[2]] = (Operation.ASSIGN, line[0])

            elif len(line) == 4: # NOT
                wires[line[3]] = (Operation.NOT, line[1])

            elif len(line) == 5: # AND, OR, LSHIFT, RSHIFT
                if line[1] == "AND":
                    wires[line[4]] = (Operation.AND, line[0], line[2])
                elif line[1] == "OR":
                    wires[line[4]] = (Operation.OR, line[0], line[2])
                elif line[1] == "LSHIFT":
                    wires[line[4]] = (Operation.LSHIFT, line[0], line[2])
                elif line[1] == "RSHIFT":
                    wires[line[4]] = (Operation.RSHIFT, line[0], line[2])
                else:
                    print("Unknown operation: {}".format(line[1]))
                    exit()

        
def get_value(wire):
    if wire.isdigit():
        return int(wire)

    if wire in cache:
        return cache[wire]

    operation = wires[wire][0]

    if operation == Operation.ASSIGN:
        value = get_value(wires[wire][1])

    elif operation == Operation.NOT:
        value = ~get_value(wires[wire][1])

    elif operation == Operation.AND:
        value = get_value(wires[wire][1]) & get_value(wires[wire][2])

    elif operation == Operation.OR:
        value = get_value(wires[wire][1]) | get_value(wires[wire][2])

    elif operation == Operation.LSHIFT:
        value = get_value(wires[wire][1]) << get_value(wires[wire][2])

    elif operation == Operation.RSHIFT:
        value = get_value(wires[wire][1]) >> get_value(wires[wire][2])

    else:
        print("Unknown operation: {}".format(operation))
        exit()

    cache[wire] = value
    return value

if __name__ == "__main__":
    INPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "input.txt")

    # Check if the input file exists
    if not os.path.exists(INPUT_PATH):
        print("Input file not found.")
        exit()

    parse_input(INPUT_PATH)

    # print("The value of wire a is {}.".format(get_value("a")))

    # Part 2

    wires["b"] = (Operation.ASSIGN, str(get_value("a")))

    cache = {}
    print("The value of wire a is {}.".format(get_value("a")))