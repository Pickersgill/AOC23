import numpy as np
import time
from functools import cache

src = "./day14_input.txt"

test = [
"O....#....",
"O.OO#....#",
".....##...",
"OO.#O....O",
".O.....O#.",
"O.#..O.#.#",
"..O..#O..O",
".......O..",
"#....###..",
"#OO..#....",
]

with open(src) as data:
    grid = np.array([list(l.strip()) for l in data.readlines()])
    #grid = np.array([list(l.strip()) for l in test])


def load(g):
    l = 0
    for i,row in enumerate(g):
        for rock in row:
            if rock == "O":
                l+=g.shape[0]-i
    return l

def tilt(g):
    ng = np.zeros(g.shape).astype(str)
    for col in range(g.shape[1]):
        current_col = g[:,col]
        for pos,rock in enumerate(current_col):
            if rock == "O":
                d = 1
                while pos-d >= 0 and current_col[pos-d] == ".":
                    d += 1
                if d > 1:
                    current_col[pos] = "."
                    current_col[pos-(d-1)] = "O"

        ng[:,col] = current_col
    return ng

def n_tilt(g):
    return tilt(g)

def s_tilt(g):
    return np.flipud(tilt(np.flipud(g)))

def w_tilt(g):
    return tilt(g.T).T

def e_tilt(g):
    return np.flipud(tilt(np.flipud(g.T))).T

cache = {}
def do_tilt(d, g, s, use_cache=True):
    h = hash_g(g)
    if use_cache and (d, h) in cache.keys():
        g, s = cache[(d, h)]
        return g, s

    if d == "E":
        ng = e_tilt(g)
    elif d == "W":
        ng = w_tilt(g)
    elif d == "S":
        ng = s_tilt(g)
    elif d == "N":
        ng = n_tilt(g)
    else:
        print("BAD DIR", d)
        exit()

    cache[(d, h)] = (ng, s)
    return ng, -1

def hash_g(g):
    row = tuple(g.flatten())
    return row

cycle = "NWSE"

def do(cycles, g, skipped=False):
    t = time.time()
    T = cycles * 4
    steps = 0
    while steps < T:
        d = cycle[steps%4]
        g, loop = do_tilt(cycle[steps%4], g, steps)
        if loop > 0:
            loop_size = steps-loop
            steps += 1
            break
        steps += 1

    steps += ((T-steps) // loop_size) * loop_size
    while steps < T:
        d = cycle[steps%4]
        g, loop = do_tilt(cycle[steps%4], g, steps, False)
        steps += 1

    return g

def pretty(g):
    print("-"*50)
    print("\n".join(["".join(l) for l in g]))
    print("-"*50)

g1 = grid.copy()
t = 1000000000
g1 = do(t, g1)
pretty(g1)
print(load(g1))


