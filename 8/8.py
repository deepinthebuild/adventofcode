import re

rawdata=[]
with open("input.txt", "rb") as data:
    for line in data:
        rawdata.append(line[:-1])
        
total = sum(len(foo) - len(eval(foo)) for foo in rawdata)
other = sum(len(re.escape(foo)) + 2 - len(foo) for foo in rawdata)

print(total)
print(other)