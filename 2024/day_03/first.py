import os
import re

input = open(os.path.join(os.path.dirname(
    os.path.realpath(__file__)), "input.txt"), "r").read()

muls = re.findall("mul\([0-9][0-9]*,[0-9][0-9]*\)", input)

sum = 0
for mul in muls:
    numbers = [int(num) for num in re.findall("\d+", mul)]
    sum += numbers[0] * numbers[1]

print(sum)
