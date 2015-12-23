import random


def replace_nth(input, old, new, n):
    if n == -1:
        n = input.count(old) - 1
    head = 0
    current = 0
    while current < n:
        head = input.find(old, head) + len(old)
        current += 1
    return input[:head] + input[head:].replace(old, new, 1)


raw_data = []
transforms = []
new_molecules = set()
original = ''

with open("input.txt", "r") as input:
    for line in input:
        raw_data.append(line[:-1])
        
original = raw_data.pop()
raw_data.pop() # trim empty entry

for entry in raw_data:
    old, new = entry.split(' => ')
    transforms.append((old,new))

for old, new in transforms:
    for k in range(original.count(old)):
        new_molecules.add(replace_nth(original, old, new, k))

print(len(new_molecules))

for _ in range(10):
    random.shuffle(transforms)
target = original
steps = 0
while target != 'e':
    for new, old in transforms:
        if old not in target:
            continue
        target = target.replace(old, new, 1)
        steps += 1
        print(target)
        random.shuffle(transforms)
        
print(steps)