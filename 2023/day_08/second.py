import os
from typing import Dict, Tuple

current_dir = os.path.dirname(os.path.realpath(__file__))
file = os.path.join(current_dir, "input.txt")

instructions = ""

paths: Dict[str, Tuple[str, str]] = {}

with open(file) as file:
    instructions = file.readline().rstrip("\n")

    line = file.readline()
    line = file.readline()

    while line:
        key_value_pair = line.rstrip("\n").split('=')
        values = key_value_pair[1].replace("(", "").replace(")", "").split(",")
        paths[key_value_pair[0].strip()] = (
            values[0].strip(), values[1].strip())
        line = file.readline()

steps = 0
current_paths = []
for p in paths:
    if p.endswith("A"):
        current_paths.append(p)

c_instructions = instructions

while True:
    side = c_instructions[0]

    if len(c_instructions) != 1:
        c_instructions = c_instructions[1:]
    else:
        c_instructions = instructions

    for i, value in enumerate(current_paths):
        choices = paths[value]

        if side == "L":
            current_paths[i] = choices[0]
        elif side == "R":
            current_paths[i] = choices[1]
        else:
            raise RuntimeError("Error in sides")

    steps += 1

    if all(p.strip().endswith("Z") for p in current_paths):
        print(steps)
        break
