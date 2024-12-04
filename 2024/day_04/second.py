import os

input_original = open(os.path.join(os.path.dirname(
    os.path.realpath(__file__)), "input.txt"), "r").read().split("\n")[:-1]

input = []
for line in input_original:
    input.append(list(line))

counter = 0

for row in range(1, len(input)-1):
    for column in range(1, len(input[row])-1):
        if input[row][column] == "A":
            if ((input[row-1][column-1] == "M" and input[row+1][column+1] == "S") or (input[row-1][column-1] == "S" and input[row+1][column+1] == "M")) and ((input[row+1][column-1] == "M" and input[row-1][column+1] == "S") or (input[row+1][column-1] == "S" and input[row-1][column+1] == "M")):
                counter += 1

print(counter)
