import numpy as np
import operator
import functools

def score(input, weights_matrix):
    input = np.array(input, dtype=np.int64)
    score = input.dot(weights_matrix)
    if np.any(score < 0):
        return 0
    else:
        return functools.reduce(operator.mul, score)
        
def score_part2(input, weights_matrix):
    input = np.array(input, dtype=np.int64)
    score = input.dot(weights_matrix)
    if np.any(score < 0):
        return 0
    elif score[-1] != 500:
        return 0
    else:
        return functools.reduce(operator.mul, score[:-1])
        
def partitions():
    for x in range(101):
        for y in range(101-x):
            for z in range((101-x)-y):
                for q in range(((101-x)-y)-z):
                    yield x,y,z,q

regex = r'\w+: capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (\d+)'

weights = np.fromregex('input.txt', regex, np.int64)
weights_no_cals = weights[:, :4]

print(max(score(split, weights_no_cals) for split in partitions()))
print(max(score_part2(split, weights) for split in partitions()))