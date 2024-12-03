import os
import re

script_dir = os.path.dirname(os.path.realpath(__file__))

file_name = "input.txt"

file_path = os.path.join(script_dir, file_name)

seeds_str = ""


def get_numbers(line):
    return list(map(int, re.findall(r'\d+'), line))

seed_to_soil = [] 
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []
try:
    with open(file_path, "r") as file:
        current_map = ""

        line = file.readline()
        line = line.split(":")[1]
        seeds_str = line
        line = file.readline()
        line = file.readline()

        while line:
            if re.match(r'[a-zA-Z]', line):
                current_map = line.split("-")[0]
            else:
                row_numbers = re.findall(r'\d+', line)

            
            
            line = file.readline()

except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(e)

"""
first_word = line.split("-")[0]
                match first_word:
                    case "seed":
                        pass
                    case "fertilizer":
                        pass
                    case "water":
                        pass
                    case "light":
                        pass
                    case "tempterature":
                        pass
                    case "humidity":
                        pass
                    case _:
                        pass
                        """