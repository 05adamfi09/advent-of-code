import os
import re

input = open(os.path.join(os.path.dirname(
    os.path.realpath(__file__)), "input.txt"), "r").read()

sections = re.split("(don't\(\))|(do\(\))", input)
muls = []
previous_section = "do()"

for section in sections:
    if previous_section == "do()":
        muls += re.findall("mul\([0-9][0-9]*,[0-9][0-9]*\)", section)
    previous_section = section

sum = 0
for mul in muls:
    numbers = [int(num) for num in re.findall("\d+", mul)]
    sum += numbers[0] * numbers[1]

print(sum)
