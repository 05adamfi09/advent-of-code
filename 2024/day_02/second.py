import os
import re

input = open(os.path.join(os.path.dirname(
    os.path.realpath(__file__)), "input.txt"), "r")

safe_reports = 0
for line in input:
    levels = [int(num) for num in re.findall("\d+", line)]

    if levels[0] < levels[1]:
        def comparator(a, b): return a < b
    else:
        def comparator(a, b): return a > b

    safe_report = True
    try_fix = False
    for i in range(len(levels)-1):
        if not (comparator(levels[i], levels[i+1]) and (1 <= abs(levels[i]-levels[i+1]) <= 3)):
            try_fix = True
            break

    if try_fix:
        possible_safe_variants = len(levels)
        for l in range(len(levels)):
            fixed_levels = levels[:]
            fixed_levels.pop(l)

            if fixed_levels[0] < fixed_levels[1]:
                def comparator(a, b): return a < b
            else:
                def comparator(a, b): return a > b

            for i in range(len(fixed_levels)-1):
                if not (comparator(fixed_levels[i], fixed_levels[i+1]) and (1 <= abs(fixed_levels[i]-fixed_levels[i+1]) <= 3)):
                    possible_safe_variants -= 1
                    break

        if possible_safe_variants == 0:
            safe_report = False

    if safe_report:
        safe_reports += 1

print(safe_reports)
