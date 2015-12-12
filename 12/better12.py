import json
import functools

@functools.singledispatch
def json_sum(input, stopword=None):
    if stopword is not None and stopword in input.values():
        return 0
    else:
        return json_sum(list(input.values()), stopword=stopword)

@json_sum.register(int)
def _(input, stopword=None):
    return input
    
@json_sum.register(str)
def _(input, stopword=None):
    return 0

@json_sum.register(list)
def _(input, stopword=None):
    return sum(json_sum(item, stopword=stopword) for item in input)
        
        
        
with open("input.txt") as input:    
    data = json.load(input)


print(json_sum(data))
print(json_sum(data, stopword="red"))

