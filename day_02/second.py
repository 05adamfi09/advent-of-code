import os

script_dir = os.path.dirname(os.path.realpath(__file__))

file_name = "input.txt"

file_path = os.path.join(script_dir, file_name)

sum = 0

try:
    with open(file_path, "r") as file:
        line = file.readline()

        while line:

            line = line.split(":")
            line = line[1]

            turns = line.split(";")

            red = 0
            green = 0
            blue = 0

            for turn in turns:
                picks = turn.split(",")

                for pick in picks:
                    number_match = []
                    for char in pick:
                        if char.isdigit():
                            number_match.append(char)
                    num_str = ""
                    for nm in number_match:
                        num_str += nm
                    final_number: int = int(num_str)

                    if "red" in pick and final_number > red:
                        red = final_number 
                    if "green" in pick and final_number > green:
                        green = final_number
                    if "blue" in pick and final_number > blue:
                        blue = final_number
                
            power_of_minimal_cubes = red * green * blue
            sum += power_of_minimal_cubes
            
            line = file.readline()

except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(e)

print(sum)