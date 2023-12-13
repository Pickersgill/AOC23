import numpy as np
src = "./day13_input.txt"

test = [
"#.##..##.",
"..#.##.#.",
"##......#",
"##......#",
"..#.##.#.",
"..##..##.",
"#.#.##.#.",
"\n",
"#...##..#",
"#....#..#",
"..##..###",
"#####.##.",
"#####.##.",
"..##..###",
"#....#..#",
]

with open(src) as data:
    #lines = [l.strip() for l in test]
    lines = [l.strip() for l in data.readlines()]
    grids = []
    cg = []

    for l in lines:
        if l:
            cg += [list(l)]
        else:
            grids += [(np.array(cg) == "#").astype(int)]
            cg = []
    grids += [np.array(cg)]
    cg = []

# Must identify any reflection point which reaches at least one edge
def vertical(grid):
    #rev = np.array([r[::-1] for r in grid])

    for pivot in range(1,grid.shape[1]):
        left = grid[:, :pivot]
        right = np.array([r[::-1] for r in grid[:, pivot:]])

        if left.shape[1] > right.shape[1]:
            left = left[:, -right.shape[1]:]
        elif right.shape[1] > left.shape[1]:
            right = right[:, -left.shape[1]:]
    
        if np.all(left==right):
            print("PIVOT AT", pivot)
            return pivot

    return 0

def horizontal(grid):
    #rev = np.array([r[::-1] for r in grid])
    grid = grid.T

    for pivot in range(1,grid.shape[1]):
        left = grid[:, :pivot]
        right = np.array([r[::-1] for r in grid[:, pivot:]])

        if left.shape[1] > right.shape[1]:
            left = left[:, -right.shape[1]:]
        elif right.shape[1] > left.shape[1]:
            right = right[:, -left.shape[1]:]
    
        if np.all(left==right):
            print("PIVOT AT", pivot)
            return pivot

    return 0

hoz = 0
vez = 0

for grid in grids:
    v = vertical(grid)
    if v:
        vez += v
    else:
        h = horizontal(grid)
        if h == 0:
            print("BAD")
        hoz += h

print(hoz, vez)
t = 100 * hoz + vez
print(t)
