with open("input.txt", "r") as infile:
    data = infile.read()
    
data = list(data)
floor = 0

for position, entry in enumerate(data):
    if entry == '(':
        floor += 1
    elif entry == ')':
        floor -= 1
    
    if floor < 0:
        print(position + 1)
        break
