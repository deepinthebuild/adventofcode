from scipy.ndimage.filters import convolve as convolve
import numpy as np


def game_of_life(input_grid):
    life_kernel = np.array([[1, 1, 1],
                            [1, 0, 1],
                            [1, 1, 1]])
    neighbors_sum = convolve(input_grid, life_kernel, mode='constant')
    output_grid = np.logical_and(input_grid == 1, neighbors_sum == 2)
    output_grid = np.logical_or(neighbors_sum == 3, output_grid)
    
    return output_grid.astype(np.int)

def game_of_life2(input_grid):
    life_kernel = np.array([[1, 1, 1],
                            [1, 0, 1],
                            [1, 1, 1]])
    neighbors_sum = convolve(input_grid, life_kernel, mode='constant')
    output_grid = np.logical_and(input_grid == 1, neighbors_sum == 2)
    output_grid = np.logical_or(neighbors_sum == 3, output_grid)
    output_grid[0,0] = 1
    output_grid[-1,0] = 1
    output_grid[0,-1] = 1
    output_grid[-1,-1] = 1
    return output_grid.astype(np.int)


def simulate(input_grid, steps):
    for _ in range(steps):
        input_grid = game_of_life(input_grid)
    return input_grid

    
def simulate2(input_grid, steps):
    for _ in range(steps):
        input_grid = game_of_life2(input_grid)
    return input_grid
    
    
grid = []
with open("input.txt", "r") as input:
    for line in input:
        out = []
        for char in line:
            if char == '#':
                out.append(1)
            elif char == '.':
                out.append(0)
        grid.append(out)

grid1 = np.array(grid)
grid2 = grid1.copy()
grid2[0,0] = 1
grid2[-1,0] = 1
grid2[0,-1] = 1
grid2[-1,-1] = 1

grid1 = simulate(grid1, 100)
print(sum(sum(grid1)))

grid2 = simulate2(grid2, 100)
print(sum(sum(grid2)))
            