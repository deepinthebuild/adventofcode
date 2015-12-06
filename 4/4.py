from hashlib import md5

def starts_with_5_zeros(input_str):
    if input_str[0:5] == '00000':
        return True
    else:
        return False

def starts_with_6_zeros(input_str):
    if input_str[0:6] == '000000':
        return True
    else:
        return False

def combine_and_hash(number):
    PUZZLE_SEED = 'bgvyzdsv'
    number_str = str(number)
    PUZZLE_KEY = PUZZLE_SEED + number_str
    PUZZLE_KEY = PUZZLE_KEY.encode('ascii')
    return md5(PUZZLE_KEY).hexdigest()
 

 
n = 0
while not starts_with_5_zeros(combine_and_hash(n)):
    n += 1
    
print("Your five zero magic number is: ", n)

k = 0
while not starts_with_6_zeros(combine_and_hash(k)):
    k += 1

print("Your six zero magic number is: ", k)