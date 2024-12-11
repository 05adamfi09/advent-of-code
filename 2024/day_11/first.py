import os
from itertools import combinations

input = open(os.path.join(os.path.dirname(
    os.path.realpath(__file__)), "input.txt"), "r").read().split("\n")[:-1][0].split(" ")

for i in range(75):
    index = 0
    len_inputs = len(input)
    while index < len_inputs:
        if int(input[index]) == 0:
            input[index] = str(1)
        elif len(input[index]) % 2 == 0:
            num_half_len = int(len(input[index])/2)
            first_half_num = input[index][:num_half_len]
            second_half_num = input[index][num_half_len:]
            input[index] = first_half_num
            if index+1 in range(len(input)):
                input.insert(index+1, str(int(second_half_num)))
            else:
                input.append(str(int(second_half_num)))
            index += 1
            len_inputs += 1
        else:
            input[index] = str(int(input[index])*2024)

        index += 1

print(len(input))
