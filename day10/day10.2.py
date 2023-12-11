from PIL import Image
import numpy as np
"""
| = vertical
- = horizontal
L = north to east
J = north to west
7 = south to west
F = south to east
. = ground/empty
S = start

FARTHEST FROM S IN STEPS FROM S (max(loop_len, loop_len-x) for x in loop)

"""
class Grid(list):
    def __init__(self, vals):
        self.h = len(vals)
        self.w = len(vals[0])
        super().__init__(vals)

    def gr(self, x, y, dx, dy):
        return list([[self.at([nx, ny]) for nx in range(x,x+dx)] for ny in range(y,y+dy)])

    def at(self, p):
        return self[p[1]][p[0]]

grid = None
S_TYPE = "L"
src = "./day10_input.txt"
with open(src) as data:
    grid = Grid([list(l.strip()) for l in data.readlines()])

def find_start(g):
    for i, row in enumerate(g):
        for j, val in enumerate(row):
            if val == "S":
                return (j,i)

def move(pos, act, heading):
    match (act, heading):
        case ("S", _):
            return move(pos, S_TYPE, heading)

        case ("J", "E"):
            return (pos[0],pos[1]-1), "N"
        case ("J", "S"):
            return (pos[0]-1,pos[1]), "W"

        case ("L", "W"):
            return (pos[0],pos[1]-1), "N"
        case ("L", "S"):
            return (pos[0]+1,pos[1]), "E"

        case ("7", "N"):
            return (pos[0]-1,pos[1]), "W"
        case ("7", "E"):
            return (pos[0],pos[1]+1), "S"
        
        case ("F", "N"):
            return (pos[0]+1,pos[1]), "E"
        case ("F", "W"):
            return (pos[0],pos[1]+1), "S"

        case ("|", "N"):
            return (pos[0],pos[1]-1), "N"
        case ("|", "S"):
            return (pos[0],pos[1]+1), "S"

        case ("-", "E"):
            return (pos[0]+1,pos[1]), "E"
        case ("-", "W"):
            return (pos[0]-1,pos[1]), "W"

        case _:
            print("BAD MOVE IN SEQ", pos, act)
            exit()

    return pos

steps = 0
pos = find_start(grid)
dists = [0]
loop = [pos]
heading = "W"
while steps == 0 or not grid.at(pos) == "S":
    pos, heading = move(pos,grid.at(pos), heading)
    steps += 1
    loop.append(pos)
    dists.append(steps)

WIDTH = len(grid[0])
HEIGHT = len(grid)

new_grid = np.zeros((WIDTH*3,HEIGHT*3))

patterns = {
    "J" : np.array([[0,1,0],[1,1,0],[0,0,0]]),
    "L" : np.array([[0,1,0],[0,1,1],[0,0,0]]),
    "7" : np.array([[0,0,0],[1,1,0],[0,1,0]]),
    "F" : np.array([[0,0,0],[0,1,1],[0,1,0]]),
    "-" : np.array([[0,0,0],[1,1,1],[0,0,0]]),
    "|" : np.array([[0,1,0],[0,1,0],[0,1,0]]),
}

start = None

for x in range(0, WIDTH):
    for y in range(0, HEIGHT):
        pattern = np.zeros((3,3))
        if (x, y) in loop:
            if not start:
                start = (y*3+2, x*3+2)
            symbol = grid.at((x,y))
            if symbol == "S":
                pattern = patterns[S_TYPE]
            else:
                pattern = patterns[symbol]

        for dx in range(3):
            for dy in range(3):
                new_grid[3*x+dx,3*y+dy] = pattern[dy,dx]
print(start)

def flood(start, G, wall=1):
    F = [start]
    V = set()
    while len(F) > 0:
        x, y = F.pop()
        V.add((x,y))
        for dx, dy in [[1,0],[0,1],[-1,0],[0,-1]]:
            n = (x+dx,y+dy)
            valid = n[0] >= 0 and n[0] < G.shape[1] and n[1] >= 0 and n[1] < G.shape[0]
            if valid and G[n[1]][n[0]] != wall and n not in V:
                F += [n]
    return V

#img = Image.new("RGB", (WIDTH, HEIGHT), "#ffffff")
outer = flood((0,0), new_grid)
for fx,fy in outer:
    new_grid[fy][fx] = 1

img = Image.fromarray(new_grid * 255)
img = img.convert("RGB")

fill = flood(start, new_grid)

for fx,fy in fill:
    img.putpixel((fx,fy), (0,255,0))

total = 0
for x in range(1, new_grid.shape[0], 3):
    for y in range(1, new_grid.shape[1], 3):
        if new_grid[y][x] != 1:
            img.putpixel((x,y), (255,0,0))
            total += 1
print(total)

img.show()
