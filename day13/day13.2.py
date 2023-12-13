import numpy as np
src = "./day13_input.txt"
with open(src) as data:
    lines = [l.strip() for l in data.readlines()]
    grids = []
    cg = []

    for l in lines:
        if l:
            cg += [list(l)]
        else:
            grids += [(np.array(cg) == "#").astype(int)]
            cg = []
    grids += [(np.array(cg) == "#").astype(int)]
    cg = []

# Must identify any reflection point which reaches at least one edge
def reflect(grid, hoz=False):
    if hoz:
        grid = grid.T

    for pivot in range(1,grid.shape[1]):
        left = grid[:, :pivot]
        right = np.array([r[::-1] for r in grid[:, pivot:]])

        if left.shape[1] > right.shape[1]:
            left = left[:, -right.shape[1]:]
        elif right.shape[1] > left.shape[1]:
            right = right[:, -left.shape[1]:]
    
        if np.sum((left!=right).astype(int)) == 1:
            return pivot

    return 0

hoz = 0
vez = 0

for i,grid in enumerate(grids):
    v = reflect(grid)
    if v:
        vez += v
    else:
        h = reflect(grid, True)
        hoz += h

t = 100 * hoz + vez
print("TOTAL", t)
