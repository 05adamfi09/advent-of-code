import os

script_dir = os.path.dirname(os.path.realpath(__file__))

file_name = "input.txt"

file_path = os.path.join(script_dir, file_name)

result = 0

try:
    with open(file_path, "r") as file:
        line = file.readline()

        while line:
            numbers_string = ""
            for char in line:
                if char.isdigit() == True:
                    numbers_string += char
            
            my_number = numbers_string[0] + numbers_string[-1]
            number_int = int(my_number)
            result += number_int
            line = file.readline()

except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(e)

print(result)

