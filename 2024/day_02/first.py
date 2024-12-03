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

    is_report_safe = True
    for i in range(len(levels)-1):
        if not (comparator(levels[i], levels[i+1]) and (1 <= abs(levels[i]-levels[i+1]) <= 3)):
            is_report_safe = False
            break

    if is_report_safe:
        safe_reports += 1

print(safe_reports)
