def has_3_vowels(input_str):
    VOWELS = 'aeiou'
    vowel_count = 0
    for test_char in input_str:
        if test_char in VOWELS:
            vowel_count += 1
            
    if vowel_count >= 3:
        return True
    else:
        return False

        
def has_bad_bits(input_str):
    NAUGHTY_BITS = ['ab', 'cd', 'pq', 'xy']
 
    for BIT in NAUGHTY_BITS:
        if BIT in input_str:
            return True
    
    return False
    
    
def has_doubled_letter(input_str):
    for j in range(len(input_str) - 1):
        if input_str[j] == input_str[j+1]:
            return True
    
    return False
    

def nice_string(input_str):
    if has_bad_bits(input_str):
        return False
    elif has_3_vowels(input_str) and has_doubled_letter(input_str):
        return True
    else:
        return False

        
def has_doubled_pair(input_str):
        for k in range(len(input_str) - 2):
            if input_str[k:k+2] in input_str[:k] or input_str[k:k+2] in input_str[k+2:]:
                return True
        
        return False
        
        
def has_skipped_repeat(input_str):
    for k in range(len(input_str) - 2):
        if input_str[k] == input_str[k+2]:
            return True
            
    return False
            
           
def nicer_string(input_str):
    if has_doubled_pair(input_str) and has_skipped_repeat(input_str):
        return True
    else:
        return False
        
        
nice_line_count = 0
nicer_line_count = 0
with open("input.txt", "r") as input:
    for line in input:
        if nice_string(line):
            nice_line_count += 1
        if nicer_string(line):
            nicer_line_count += 1
            
print("The number of nice lines is:", nice_line_count)
print("The number of nicer lines is:", nicer_line_count)