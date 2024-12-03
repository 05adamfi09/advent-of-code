import os
import re

script_dir = os.path.dirname(os.path.realpath(__file__))

file_name = "input.txt"

file_path = os.path.join(script_dir, file_name)

winning_points = 0

try:
    with open(file_path, "r") as file:
        line = file.readline()

        while line:
            winning_numbers = line.split("|")[0].split(":")[1]
            my_numbers = line.split("|")[1]
            
            winning_numbers = re.findall(r'\d+', winning_numbers)
            my_numbers = re.findall(r'\d+', my_numbers)
            
            card_winning_numbers = 0

            for winning_number in winning_numbers:
                counter = my_numbers.count(winning_number)
            
                card_winning_numbers += counter
            
            card_winning_points = 0

            if card_winning_numbers > 0:
                card_winning_numbers -= 1
                card_winning_points = 1
            
            for i in range(card_winning_numbers):
                card_winning_points = card_winning_points * 2
                
            winning_points += card_winning_points
            
            line = file.readline()

except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(e)

print(winning_points)