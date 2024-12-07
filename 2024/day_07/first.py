import os
from itertools import product

input = open(os.path.join(os.path.dirname(
    os.path.realpath(__file__)), "input.txt"), "r").read().split("\n")[:-1]


def add_parentheses(numbers, operators):
    expression = str(numbers[0])
    for i in range(len(operators)):
        expression = f"({expression} {operators[i]} {numbers[i+1]})"
    return expression


calibration_result = 0

for line in input:
    test_value, numbers_part = line.split(": ")
    numbers_str = numbers_part.split(" ")
    numbers = [int(item) for item in numbers_str]
    combinations = list(product(["+", "*"], repeat=len(numbers)-1))

    for combo in combinations:
        expression = add_parentheses(numbers, combo)
        try:
            result = eval(expression)
            if result == int(test_value):
                calibration_result += int(test_value)
                break
        except Exception as e:
            print(f"Evaluation error {expression}: {e}")

print(calibration_result)
