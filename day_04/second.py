import os
import re

script_dir = os.path.dirname(os.path.realpath(__file__))

file_name = "input.txt"

file_path = os.path.join(script_dir, file_name)

#209 lines
list_of_scratches = [1] * 209

try:
    with open(file_path, "r") as file:
        line = file.readline()
        current_line = 0

        while line:
            winning_numbers = line.split("|")[0].split(":")[1]
            my_numbers = line.split("|")[1]
            
            winning_numbers = re.findall(r'\d+', winning_numbers)
            my_numbers = re.findall(r'\d+', my_numbers)
            
            for scratch in range(list_of_scratches[current_line]):

                card_winning_numbers = 0

                for winning_number in winning_numbers:
                    counter = my_numbers.count(winning_number)
                
                    card_winning_numbers += counter


                for i in range(card_winning_numbers):
                    list_of_scratches[current_line+1+i] = list_of_scratches[current_line+1+i] + 1
                
            current_line += 1
            line = file.readline()

except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(e)

print(sum(list_of_scratches))