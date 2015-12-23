import numpy as np
import numba


INPUT = 34000000

@numba.jit
def part1(target):
    houses = np.zeros(target//10, dtype=np.int)
    for elf in range(1,target//10):
        houses[elf::elf] += elf*10
    return np.flatnonzero(houses >= target)[0]
    
@numba.jit
def part2(target):
    houses = np.zeros(target//10, dtype=np.int)
    for elf in range(1,target//10):
        houses[elf:50*(elf+1):elf] += elf*11
    return np.flatnonzero(houses >= target)[0]
    
print(part1(INPUT))
print(part2(INPUT))