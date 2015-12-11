from itertools import groupby


def increment(input_str):
    input_list = [ord(x) - 97 for x in input_str]
    input_list[-1] += 1
    while any(element >= 26 for element in input_list):
        for index, item in enumerate(input_list):
            if item >= 26:
                input_list[index] -= 26
                input_list[index - 1] += 1
    return "".join(chr(x + 97) for x in input_list)
    

def has_bad_letters(input_str):
    bad_letters = 'iol'
    for letter in bad_letters:
        if letter in input_str:
            return True
    return False

        
def has_straight(input_str):
    input_list = [ord(x) - 97 for x in input_str]
    
    for index in range(len(input_list) - 2):
        if input_list[index] == input_list[index+1] - 1 == input_list[index+2] - 2:
            return True
            
    return False

    
def has_pairs(input_str):
    group_sizes = []
    for key, group in groupby(input_str):
        group_sizes.append(len(list(group)))
    if group_sizes.count(4) > 0:
        return True
    elif group_sizes.count(2) >= 2:
        return True
    else:
        return False
        
        
def password_check(input_str):
    if has_bad_letters(input_str):
        return False
    elif has_straight(input_str) and has_pairs(input_str):
        return True
    else:
        return False

        
input = "hepxcrrq"

while not password_check(input):
    input = increment(input)

print(input)

input = increment(input)

while not password_check(input):
    input = increment(input)
    
print(input)
