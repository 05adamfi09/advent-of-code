import os

input = open(os.path.join(os.path.dirname(
    os.path.realpath(__file__)), "input.txt"), "r")

left_list: list[int] = []
right_list: list[int] = []

for line in input:
    numbers = line.split("   ")
    left_list.append(int(numbers[0]))
    right_list.append(int(numbers[1]))

distance = 0

for n in left_list:
    distance += n * right_list.count(n)

print(distance)
