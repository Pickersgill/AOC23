import numpy as np
from functools import cache
src = "./day21_input.txt"

with open(src) as data:
    grid = np.array([list(l.strip()) for l in data.readlines()])
    H, W = grid.shape

@cache
def get_neighbours(point):
    ns = []
    for dx, dy in [[1,0],[0,1],[-1,0],[0,-1]]:
        x = dx+point[0]
        y = dy+point[1]
        if 0 <= x < W and 0 <= y < H and grid[y,x] != "#":
            ns.append((x,y))
    return ns

def get_points(start, after):
    F = [start]
    for i in range(after):
        nF = []
        for p in F:
            nF += get_neighbours(p)
        F = list(set(nF))
    return F

start = np.where(grid=="S")
start = (start[0][0],start[1][0])

s = get_points(start, 64)
print(len(s))

