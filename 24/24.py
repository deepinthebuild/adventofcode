import functools as fn
import itertools as it
import operator as op

def santa_splits(groups): 
    w = sum(data) // groups
    for x in range(len(data)):
        group1 = [fn.reduce(op.mul, foo) for foo in it.combinations(data, x) if sum(foo) == w]
        if group1:
            return min(group1)


data = []
with open("input.txt", "r") as input:
    for line in input:
        data.append(int(line))

print(santa_splits(3))
print(santa_splits(4))
