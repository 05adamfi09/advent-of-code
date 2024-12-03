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

while left_list:
    distance += abs(min(left_list) - min(right_list))
    left_list.remove(min(left_list))
    right_list.remove(min(right_list))

print(distance)
