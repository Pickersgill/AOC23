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
            return [pos[0],pos[1]-1], "N"
        case ("J", "S"):
            return [pos[0]-1,pos[1]], "W"

        case ("L", "W"):
            return [pos[0],pos[1]-1], "N"
        case ("L", "S"):
            return [pos[0]+1,pos[1]], "E"

        case ("7", "N"):
            return [pos[0]-1,pos[1]], "W"
        case ("7", "E"):
            return [pos[0],pos[1]+1], "S"
        
        case ("F", "N"):
            return [pos[0]+1,pos[1]], "E"
        case ("F", "W"):
            return [pos[0],pos[1]+1], "S"

        case ("|", "N"):
            return [pos[0],pos[1]-1], "N"
        case ("|", "S"):
            return [pos[0],pos[1]+1], "S"

        case ("-", "E"):
            return [pos[0]+1,pos[1]], "E"
        case ("-", "W"):
            return [pos[0]-1,pos[1]], "W"

        case _:
            print("BAD MOVE IN SEQ", pos, act)
            exit()
            

    return pos

steps = 0
pos = find_start(grid)
dists = [0]
loop = [pos]
heading = "W"
print(pos)
while steps == 0 or not grid.at(pos) == "S":
    pos, heading = move(pos,grid.at(pos), heading)
    if steps < 10:
        print(pos)
    steps += 1
    dists.append(steps)

print("\n".join([str(s) for s in grid.gr(pos[0]-5,pos[1]-5,10,10)]))

dists_from_start = [min(d, len(dists)-d) for d in dists]
print(dists_from_start[0:5])
print(dists_from_start[-5:])
print(max(dists_from_start))


