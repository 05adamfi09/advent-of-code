import os
from dataclasses import dataclass

script_dir = os.path.dirname(os.path.realpath(__file__))

file_name = "input.txt"

file_path = os.path.join(script_dir, file_name)


def char_frequention(input_str):
    char_count = {}

    for char in input_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    sorted_chars = sorted(char_count, key=lambda x: char_count[x], reverse=True)

    most_frequented = sorted_chars[0]

    if len(char_count) > 1:
        second_frequented = sorted_chars[1] 
        second_frequented_count = char_count.get(second_frequented)
    else:
        second_frequented = None
        second_frequented_count = None
    
    
    return most_frequented, char_count.get(most_frequented), second_frequented, second_frequented_count

@dataclass
class Hand:
    type: int
    hand : str
    bid: int


hand_list = []

try:
    with open(file_path, "r") as file:
        line = file.readline()
        i = 0
        while line:
            
            bid = int(line.split(" ")[1])
            line = line.split(" ")[0]

            most_frequented, most_frequented_count, second_frequented, second_frequented_count = char_frequention(line)

            
            if "J" in line:
                J_counter = line.count("J")
                if "J" != most_frequented:
                    for i in range(J_counter):
                        most_frequented_count += 1
                    print(most_frequented_count)
                elif second_frequented_count is not None:
                    most_frequented_count = second_frequented_count
                    for i in range(J_counter):
                        most_frequented_count += 1

            if most_frequented_count == 5:
                type = 7
            elif most_frequented_count == 4:
                type = 6
            elif most_frequented_count == 3 and second_frequented_count == 2:
                type = 5
            elif most_frequented_count == 3:
                type = 4
            elif most_frequented_count == 2 and second_frequented_count == 2:
                type = 3
            elif most_frequented_count == 2:
                type = 2
            else:
                type = 1

            

            hand = Hand(type, line, bid)

            hand_list.append(hand)

            i += 1
            line = file.readline()

except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(e)


char_order_mapping = {'A': 13, 'K': 12, 'Q': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1}
def custom_sort_key(hand):
    return hand.type, [char_order_mapping.get(char) for char in hand.hand]

ordered_hands = sorted(hand_list, key=custom_sort_key)

sum = 0
multiplier = 1

for hand in ordered_hands:    
    sum += hand.bid * multiplier
    multiplier += 1

print(sum)