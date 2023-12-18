from PIL import Image, ImageDraw
import numpy as np
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
    moves = [l.strip().split() for l in data]
    t_moves = [l.strip().split() for l in test]


d_map = {"R": (1,0), "D": (0,1), "L": (-1,0), "U": (0,-1)}

def explore(ms):
    pos = (0,0)

    path = [pos]
    for m in ms:
        dx, dy = d_map[m[0]]
        for dist in range(int(m[1])):
            pos = (pos[0]+dx, pos[1]+dy)
            path += [pos]

    return path

def show_path(path):
    maxx = max(path, key=lambda x : x[0])[0]+1
    maxy = max(path, key=lambda x : x[1])[1]+1
    minx = min(path, key=lambda x : x[0])[0]
    miny = min(path, key=lambda x : x[1])[1]
    img = Image.new("1", (maxx-minx, maxy-miny))
    draw = ImageDraw.Draw(img)
    draw.polygon([(p[0]-minx,p[1]-miny) for p in path], outline="red", fill=1)
    img.save("out.png")
    return np.array(img).astype(int)

path = explore(moves)
pmap = show_path(path)
t = np.sum(pmap)
print(t)




