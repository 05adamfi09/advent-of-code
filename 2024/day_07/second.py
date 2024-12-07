import os
from itertools import product

input = open(os.path.join(os.path.dirname(
    os.path.realpath(__file__)), "input.txt"), "r").read().split("\n")[:-1]


def evaluate_expression(expression):
    tokens = expression.split()
    result = tokens[0]
    for i in range(1, len(tokens), 2):
        operator = tokens[i]
        operand = tokens[i + 1]
        if operator == '+':
            result = str(int(result) + int(operand))
        elif operator == '*':
            result = str(int(result) * int(operand))
        elif operator == '||':
            result = result + operand
    return int(result)


calibration_result = 0

for line in input:
    test_value, numbers_part = line.split(": ")
    numbers_str = numbers_part.split(" ")
    numbers = [int(item) for item in numbers_str]
    combinations = list(product(["+", "*", "||"], repeat=len(numbers)-1))

    for combo in combinations:
        expression = " ".join(str(numbers[i]) + f" {combo[i]} " if i < len(
            combo) else str(numbers[i]) for i in range(len(numbers)))
        try:
            result = evaluate_expression(expression)
            if result == int(test_value):
                calibration_result += int(test_value)
                break
        except Exception as e:
            print(f"Evaluation error {expression}: {e}")

print(calibration_result)
