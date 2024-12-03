import os

script_dir = os.path.dirname(os.path.realpath(__file__))

file_name = "input.txt"

file_path = os.path.join(script_dir, file_name)

sum_of_ids = 0
current_id = 0

try:
    with open(file_path, "r") as file:
        line = file.readline()

        while line:
            current_id += 1

            line = line.split(":")
            line = line[1]

            turns = line.split(";")

            was_invalid = False

            for turn in turns:
                picks = turn.split(",")

                red = 0
                green = 0
                blue = 0

                for pick in picks:
                    number_match = []
                    for char in pick:
                        if char.isdigit():
                            number_match.append(char)
                    num_str = ""
                    for nm in number_match:
                        num_str += nm
                    final_number: int = int(num_str)
                    
                    if "red" in pick:
                        red += final_number
                    if "green" in pick:
                        green += final_number
                    if "blue" in pick:
                        blue += final_number
                
                if red > 12 or green > 13 or blue > 14:
                    was_invalid = True
            if was_invalid == False:
                sum_of_ids += current_id

            line = file.readline()

except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(e)

print(sum_of_ids)