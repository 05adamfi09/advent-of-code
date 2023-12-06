import os
import re

script_dir = os.path.dirname(os.path.realpath(__file__))

file_name = "input.txt"

file_path = os.path.join(script_dir, file_name)

time = 0
distance = 0

try:
    with open(file_path, "r") as file:
        line = file.readline()

        set_time = True

        while line:
            the_number = ""
            numbers = re.findall(r'\d+', line)

            for num in numbers:
                the_number += num

            if set_time:
                time = int(the_number)
                set_time = False
            else:
                distance = int(the_number)
            
            line = file.readline()

except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(e)

race_records = 0

for speed in range(time + 1):
    if speed * (time-speed) > distance:
        race_records += 1

print(race_records)
