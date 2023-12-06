import os
import re

script_dir = os.path.dirname(os.path.realpath(__file__))

file_name = "input.txt"

file_path = os.path.join(script_dir, file_name)

time = []
distance = []

try:
    with open(file_path, "r") as file:
        line = file.readline()

        set_time = True

        while line:
            my_list = []
            numbers = re.findall(r'\d+', line)

            for num in numbers:
                my_list.append(int(num))

            if set_time:
                time = my_list
                set_time = False
            else:
                distance = my_list
            
            line = file.readline()

except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(e)

num_of_distances = len(distance)

determinator = 1

for i in range(num_of_distances):
    current_time = time[i]
    current_distance = distance[i]

    race_records = 0

    for speed in range(current_time + 1):
        if speed * (current_time-speed) > current_distance:
            race_records += 1
    
    determinator *= race_records

print(determinator)
