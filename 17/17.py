import itertools as it


change = []

with open("input.txt", "r") as input:
    for entry in input:
        change.append(int(entry))

total = 0
total2 = 0
min_comb_len = 100

for r in range(len(change) + 1):
    for k in it.combinations(change, r):
        if sum(k) == 150:
            total += 1
            min_comb_len = min(min_comb_len, len(k))
            
for r in range(len(change) + 1):
    for k in it.combinations(change, r):
        if sum(k) == 150 and len(k) == min_comb_len:
            total2 += 1
            
print(total)
print(total2)