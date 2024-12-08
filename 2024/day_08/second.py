import os
from itertools import combinations

input_original = open(os.path.join(os.path.dirname(
    os.path.realpath(__file__)), "input.txt"), "r").read().split("\n")[:-1]

input: list[list[str]] = []
for l in input_original:
    input.append(list(l))

HEIGHT = len(input)
WIDTH = len(input[0])

antenas: dict[str, list[tuple[int, int]]] = {}
for r in range(len(input)):
    for c in range(len(input[r])):
        if input[r][c] != ".":
            if input[r][c] in antenas:
                antenas[input[r][c]].append((r, c))
            else:
                antenas[input[r][c]] = [(r, c)]

unique_locations: set[tuple[int, int]] = set()
for key in antenas.keys():
    for ((x1, y1), (x2, y2)) in list(combinations(antenas[key], 2)):
        x_diff = abs(x1-x2)
        y_diff = abs(y1-y2)
        unique_locations.add((x1, y1))
        unique_locations.add((x2, y2))
        if x1 < x2:
            if y1 < y2:
                while x1-x_diff >= 0 and y1 - y_diff >= 0:
                    unique_locations.add((x1-x_diff, y1 - y_diff))
                    x1 -= x_diff
                    y1 -= y_diff
                while x2+x_diff < HEIGHT and y2 + y_diff < WIDTH:
                    unique_locations.add((x2+x_diff, y2 + y_diff))
                    x2 += x_diff
                    y2 += y_diff
            else:
                while x1-x_diff >= 0 and y1 + y_diff < WIDTH:
                    unique_locations.add((x1-x_diff, y1 + y_diff))
                    x1 -= x_diff
                    y1 += y_diff
                while x2+x_diff < HEIGHT and y2 - y_diff >= 0:
                    unique_locations.add((x2+x_diff, y2 - y_diff))
                    x2 += x_diff
                    y2 -= y_diff
        else:
            if y1 < y2:
                while x1+x_diff < HEIGHT and y1 - y_diff >= 0:
                    unique_locations.add((x1+x_diff, y1 - y_diff))
                    x1 += x_diff
                    y1 -= y_diff
                while x2-x_diff >= 0 and y2 + y_diff < WIDTH:
                    unique_locations.add((x2-x_diff, y2 + y_diff))
                    x2 -= x_diff
                    y2 += y_diff
            else:
                while x1+x_diff < HEIGHT and y1+y_diff < WIDTH:
                    unique_locations.add((x1+x_diff, y1+y_diff))
                    x1 += x_diff
                    y1 += y_diff
                while x2-x_diff >= 0 and y2 - y_diff >= 0:
                    unique_locations.add((x2-x_diff, y2 - y_diff))
                    x2 -= x_diff
                    y2 -= y_diff

counter = 0
for x, y in unique_locations:
    if 0 <= x < len(input) and 0 <= y < len(input[0]):
        counter += 1

print(counter)
