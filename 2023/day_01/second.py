import os  


script_dir = os.path.dirname(os.path.realpath(__file__))

file_name = "input.txt"

file_path = os.path.join(script_dir, file_name)

result = 0

word_mapping = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight' : 8,
    'nine' : 9,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

try:
    with open(file_path, "r") as file:
        line = file.readline()
        while line:
            found_substrings = []

            for word in word_mapping:
                if word in line:
                    found_substrings.append(word)
            
            if len(found_substrings) != 0:         
                f = found_substrings[0]
                l = found_substrings[0]
                for s in range(len(found_substrings)-1):
                    s += 1
                    if line.find(found_substrings[s]) < line.find(f):
                        f = found_substrings[s]
                    if line.rfind(found_substrings[s]) > line.rfind(l):
                        l = found_substrings[s]
                
                first = str(word_mapping[f])
                last = str(word_mapping[l])                

                my_number = first + last
                
                number_int = int(my_number)

                result += number_int
            
            line = file.readline()

except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(e)

print(result)
