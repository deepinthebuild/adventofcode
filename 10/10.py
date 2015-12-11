from itertools import groupby

def conway(sequence):
    output = ""
    for key, group in groupby(sequence):
        output += str(len(list(group))) + str(key)
    return output

input = "1113122113"


for _ in range(40):
    input = conway(input)

print(len(input))

for _ in range(10):
    input = conway(input)
    
print(len(input))