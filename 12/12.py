import string
import json

def list_walk(input_list):
    values = []
    for item in input_list:
        if isinstance(item, int):
            values.append(item)
        elif isinstance(item, str):
            pass
        elif isinstance(item, list):
            values.append(list_walk(item))
        elif isinstance(item, dict):
            values.append(dict_walk(item))
    return sum(values)

def dict_walk(input_dict):
    values = []
    for key, item in input_dict.items():
        if isinstance(item, dict):
            values.append(dict_walk(item))
        elif isinstance(item, list):
            values.append(list_walk(item))
        elif isinstance(item, str):
            if item == 'red':
                return 0
            else:
                pass
        elif isinstance(item, int):
            values.append(item)
    return sum(values)
        
    
data = ""
with open("input.txt", "rt") as input:
    data = input.read()
    
    
datasum = data
for char in string.ascii_lowercase + '[]{}:"\n,':
    datasum = datasum.replace(char, " ")

datasum = [int(x) for x in datasum.split()]
print(sum(datasum))

datajson = json.loads(data)
print(dict_walk(datajson))

