def parse(input_str):
    input_parts = input_str.split()
    if 'toggle' in input_parts:
        return ('toggle', 
                tuple(int(x) for x in input_parts[1].split(',')), 
                tuple(int(x) for x in input_parts[3].split(',')))
    elif 'turn' in input_parts:
        return (input_parts[1], 
                tuple(int(x) for x in input_parts[2].split(',')), 
                tuple(int(x) for x in input_parts[4].split(',')))


lights_array = []
for _ in range(1000):
    lights_array.append([0] * 1000)

instructions = []
with open("input.txt","r") as input:
    for line in input:
        instructions.append(parse(line))


for item in instructions:
    if item[0] == 'on':
        for x in range(item[1][0], item[2][0]+1):
            for y in range(item[1][1], item[2][1]+1):
                lights_array[x][y] = 1
    elif item[0] == 'off':
        for x in range(item[1][0], item[2][0]+1):
            for y in range(item[1][1], item[2][1]+1):
                lights_array[x][y] = 0
    elif item[0] == 'toggle':
        for x in range(item[1][0], item[2][0]+1):
            for y in range(item[1][1], item[2][1]+1):
                lights_array[x][y] = int(lights_array[x][y] is not 1)

print("Number of lit lights:", sum(sum(x) for x in lights_array))

lights_array = []
for _ in range(1000):
    lights_array.append([0] * 1000)

for item in instructions:
    if item[0] == 'on':
        for x in range(item[1][0], item[2][0]+1):
            for y in range(item[1][1], item[2][1]+1):
                lights_array[x][y] += 1
    elif item[0] == 'off':
        for x in range(item[1][0], item[2][0]+1):
            for y in range(item[1][1], item[2][1]+1):
                lights_array[x][y] = max(0, lights_array[x][y]-1)
    elif item[0] == 'toggle':
        for x in range(item[1][0], item[2][0]+1):
            for y in range(item[1][1], item[2][1]+1):
                lights_array[x][y] += 2
                

print("Intensity of lit lights:", sum(sum(x) for x in lights_array))