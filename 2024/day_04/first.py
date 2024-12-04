import os

input_original = open(os.path.join(os.path.dirname(
    os.path.realpath(__file__)), "input.txt"), "r").read().split("\n")[:-1]

input = []
for line in input_original:
    input.append(list(line))


def row_counter(row_index: int, column_index: int, input: list[list[str]]) -> int:
    c = 0
    try:
        if input[row_index][column_index] == "X" and input[row_index][column_index+1] == "M" and input[row_index][column_index+2] == "A" and input[row_index][column_index+3] == "S":
            c += 1
    except IndexError:
        pass
    try:
        if input[row_index][column_index] == "X" and input[row_index][column_index-1] == "M" and input[row_index][column_index-2] == "A" and input[row_index][column_index-3] == "S" and column_index-3 >= 0:
            c += 1
    except IndexError:
        pass

    return c


def column_counter(row_index: int, column_index: int,  input: list[list[str]]) -> int:
    c = 0
    try:
        if input[row_index][column_index] == "X" and input[row_index-1][column_index] == "M" and input[row_index-2][column_index] == "A" and input[row_index-3][column_index] == "S" and row_index-3 >= 0:
            c += 1
    except IndexError:
        pass
    try:
        if input[row_index][column_index] == "X" and input[row_index+1][column_index] == "M" and input[row_index+2][column_index] == "A" and input[row_index+3][column_index] == "S":
            c += 1
    except IndexError:
        pass

    return c


def diagonal_counter(row_index: int, column_index: int,  input: list[list[str]]) -> int:
    c = 0
    try:
        if input[row_index][column_index] == "X" and input[row_index-1][column_index-1] == "M" and input[row_index-2][column_index-2] == "A" and input[row_index-3][column_index-3] == "S" and row_index-3 >= 0 and column_index-3 >= 0:
            c += 1
    except IndexError:
        pass
    try:
        if input[row_index][column_index] == "X" and input[row_index+1][column_index+1] == "M" and input[row_index+2][column_index+2] == "A" and input[row_index+3][column_index+3] == "S":
            c += 1
    except IndexError:
        pass
    try:
        if input[row_index][column_index] == "X" and input[row_index-1][column_index+1] == "M" and input[row_index-2][column_index+2] == "A" and input[row_index-3][column_index+3] == "S" and row_index-3 >= 0:
            c += 1
    except IndexError:
        pass
    try:
        if input[row_index][column_index] == "X" and input[row_index+1][column_index-1] == "M" and input[row_index+2][column_index-2] == "A" and input[row_index+3][column_index-3] == "S" and column_index-3 >= 0:
            c += 1
    except IndexError:
        pass

    return c


counter = 0

for row in range(len(input)):
    for char in range(len(input[row])):
        if input[row][char] == "X":
            counter += row_counter(row, char, input)
            counter += column_counter(row, char, input)
            counter += diagonal_counter(row, char, input)

print(counter)
