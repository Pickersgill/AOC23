from PIL import Image, ImageDraw
import numpy as np
import re
src = "day18_input.txt"

test = [
"R 6 (#70c710)",
"D 5 (#0dc571)",
"L 2 (#5713f0)",
"D 2 (#d2c081)",
"R 2 (#59c680)",
"D 2 (#411b91)",
"L 5 (#8ceee2)",
"U 2 (#caa173)",
"L 1 (#1b58a2)",
"U 2 (#caa171)",
"R 2 (#7807d2)",
"U 3 (#a77fa3)",
"L 2 (#015232)",
"U 2 (#7a21e3)",
]
with open(src) as data:
    expr = r"[RDLU] \d+ \(#([0-9a-fA-F]+)\)"
    moves = [re.match(expr, l.strip())[1] for l in data.readlines()]
    t_moves = [re.match(expr, l.strip())[1] for l in test]


d_map = {"0": (1,0), "1": (0,1), "2": (-1,0), "3": (0,-1)}

def explore(ms):
    pos = (0,0)

    path = [pos]
    for m in ms:
        dx, dy = d_map[m[-1]]
        dist = int("0x"+m[:-1], 0)
        pos = (pos[0]+dx*dist, pos[1]+dy*dist)
        path += [pos]

    return path

def shoelace(ps):
    """
    1/2 * sum(1,n) |[[xi, yi][xi+1,yi+1]]|
    where n+1 => 1
    """
    n = len(ps)
    ps = ps + [ps[0]]
    mats = [np.array([[ps[i][0],ps[i][1]],[ps[i+1][0],ps[i+1][1]]]) for i in range(n)]
    dets = [np.linalg.det(m) for m in mats]
    area = sum(dets)/2
    
    per = sum([abs(ps[i][0]-ps[i+1][0])+abs(ps[i][1]-ps[i+1][1]) for i in range(n)])/2

    return area + per + 1

path = explore(moves)
print(shoelace(path))




