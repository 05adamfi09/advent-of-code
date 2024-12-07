import os

input_original = open(os.path.join(os.path.dirname(
    os.path.realpath(__file__)), "input.txt"), "r").read().split("\n")[:-1]

input = []
for line in input_original:
    input.append(list(line))


def change_direction(current_position: str) -> tuple[str, tuple[int, int]]:
    match current_position:
        case "<":
            return "^", (-1, 0)
        case "^":
            return ">", (0, 1)
        case ">":
            return "v", (1, 0)
        case "v":
            return "<", (0, -1)
        case _:
            raise ValueError(current_position + " isn't defined.")


def find_position(input: list[list[str]]) -> tuple[int, int]:
    for line in range(len(input)):
        for column in range(len(input[line])):
            if input[line][column] in ["^", ">", "<", "v"]:
                return (line, column)
    raise IndexError("Couldn't find current position")


jorney_continues = True


row, column = find_position(input)
orientation = input[row][column]
row_move = -1
column_move = 0

while True:
    try:
        if input[row+row_move][column+column_move] != "#":
            input[row][column] = "X"
            input[row+row_move][column+column_move] = orientation
            row += row_move
            column += column_move
        else:
            (orientation, (row_move, column_move)) = change_direction(orientation)
            input[row][column] = orientation
    except IndexError:
        input[row][column] = "X"
        break

visited_places = 0
for a in input:
    visited_places += a.count("X")

print(input)
print(visited_places)
