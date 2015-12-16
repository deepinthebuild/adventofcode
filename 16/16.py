import collections
readouts = { 
            "children": 3,
            "cats": 7,
            "samoyeds": 2,
            "pomeranians": 3,
            "akitas": 0,
            "vizslas": 0,
            "goldfish": 5,
            "trees": 3,
            "cars": 2,
            "perfumes": 1
            }

def bang():
    return "!"

def query(input_dict):
    for key, value in input_dict.items():
        if value is not "!" and value != readouts[key]:
            return False
    return True

def query2(input_dict):
    for key, value in readouts.items():
        if key is "cats" or key is "trees":
            if input_dict[key] is not "!" and value >= input_dict[key]:
                return False
        elif key is "pomeranians" or key is "goldfish":
            if input_dict[key] is not "!" and value <= input_dict[key]:
                return False
        elif input_dict[key] is not "!" and value != input_dict[key]:
            return False
    return True
                
aunts = {}

with open("input.txt", "r") as input:
    for index, line in enumerate(input, start=1):
        aunts[index] = collections.defaultdict(bang)
        line = line[line.find(":")+1:]
        for blob in line.strip().split(","):
            chunks = blob.split(":")
            aunts[index][chunks[0].strip()] = int(chunks[1])

for aunt_number, aunt_dict in aunts.items():
    if query(aunt_dict):
        print(aunt_number)
        
for aunt_number, aunt_dict in aunts.items():
    if query2(aunt_dict):
        print(aunt_number)