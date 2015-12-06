with open("input.txt", "r") as datafile:
    santa_path = datafile.read()

santa_x = 0
santa_y = 0
houses = []

houses.append((santa_x, santa_y))

for char in santa_path:
    if char == '^':
        santa_y += 1
    elif char == 'v':
        santa_y -= 1
    elif char == '>':
        santa_x += 1
    elif char == '<':
        santa_x -= 1
        
    houses.append((santa_x, santa_y))
    

    
print("Houses with at least one present: ", len(set(houses)))

santa_x = 0
santa_y = 0
houses = []
houses.append((santa_x, santa_y))

for char in santa_path[::2]:
    if char == '^':
        santa_y += 1
    elif char == 'v':
        santa_y -= 1
    elif char == '>':
        santa_x += 1
    elif char == '<':
        santa_x -= 1
        
    houses.append((santa_x, santa_y))

santa_x = 0
santa_y = 0

for char in santa_path[1::2]:
    if char == '^':
        santa_y += 1
    elif char == 'v':
        santa_y -= 1
    elif char == '>':
        santa_x += 1
    elif char == '<':
        santa_x -= 1
        
    houses.append((santa_x, santa_y))

print("Houses with at least one present, including ROBO-SANTA:", len(set(houses)))
