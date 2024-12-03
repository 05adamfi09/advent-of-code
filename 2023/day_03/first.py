import os
import re
#Result should be 535351...

script_dir = os.path.dirname(os.path.realpath(__file__))

file_name = "input.txt"

file_path = os.path.join(script_dir, file_name)

matrix = []

#Getting input.txt into matrix
try:
    with open(file_path, "r") as file:
        line = file.readline()
        while line:
            row = []
            for i in range(len(line)-1):
                row.append(line[i])
            matrix.append(row)
            line = file.readline()
            

except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(e)


#Geting indexes of special symbols and list of rows (string)
basic_symbols = [".", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
special_char_indexes = []
list_of_rows = []
for i in range(len(matrix)):
    special_chars_row_indexes = []
    row_str = ""
    for j in range(len(matrix[i])):
        if matrix[i][j] not in basic_symbols:
            special_chars_row_indexes.append(j)
        row_str += matrix[i][j]
    list_of_rows.append(row_str)
    special_char_indexes.append(special_chars_row_indexes)

sum = 0

#For every row
for i in range(len(list_of_rows)):
    #Find all nums
    numbers = re.findall(r'\d+', list_of_rows[i])       
    was_counted_once = False

    #For each number in row
    for num in numbers:
        #Check if number isn't in row more than once
        number_counter = numbers.count(num)
        if number_counter > 1:
            if not was_counted_once:
                index = list_of_rows[i].find(num)
                was_counted_once = True
            else:
                index = list_of_rows[i].rfind(num)
        else:
            index = list_of_rows[i].find(num)
        number_len = len(num)
        available_positions = range(index-1, index+number_len+1)
        is_already_valid = False
        
        if i != 0:
            for special_char_index in special_char_indexes[i-1]:
                if special_char_index in available_positions:
                    sum += int(num)
                    is_already_valid = True
                    break

            
        if not is_already_valid:
            for special_char_index in special_char_indexes[i]:
                if special_char_index in available_positions:
                    sum += int(num)
                    is_already_valid = True
                    break

        if not is_already_valid:
            if i != (len(list_of_rows)-1):
                for special_char_index in special_char_indexes[i+1]:
                    if special_char_index in available_positions:
                        sum += int(num)
                        break
    
print(sum)