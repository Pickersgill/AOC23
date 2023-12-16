import numpy as np

test = [
r".|...\....",
r"|.-.\.....",
r".....|-...",
r"........|.",
r"..........",
r".........\\",
r"..../.\\..",
r".-.-/..|..",
r".|....-|.\\",
r"..//.|....",
]

energy = [
r"######....",
r".#...#....",
r".#...#####",
r".#...##...",
r".#...##...",
r".#...##...",
r".#..####..",
r"########..",
r".#######..",
r".#...#.#..",
]

src = "./day16_input.txt"

with open(src) as data:
    lines = [list(l.strip()) for l in data.readlines()]
    #lines = np.array([list(l.strip()) for l in test])

def move(pos, d):
    match d:
        case "W": return (pos[0]-1, pos[1])
        case "E": return (pos[0]+1, pos[1])
        case "N": return (pos[0], pos[1]-1)
        case "S": return (pos[0], pos[1]+1)
        case _:
            print("OOPSIE")
            exit()

def valid(pos, grid):
    H = len(grid)
    W = len(grid[0])
    return pos[0] >= 0 and pos[0] < W and pos[1] >= 0 and pos[1] < H

def next_steps(pos, d, grid):
    sym = grid[pos[1]][pos[0]]
    if sym == ".":
        return [(move(pos,d), d)]
    elif sym == "|":
        if d in "EW":
            return [(pos, "N"), (pos, "S")]
        else:
            return [(move(pos, d), d)]
    elif sym == "-":
        if d in "NS":
            return [(pos, "E"), (pos, "W")]
        else:
            return [(move(pos, d), d)]
    elif sym == "/":
        match d:
            case "W": return [(move(pos, "S"), "S")]
            case "E": return [(move(pos, "N"), "N")]
            case "N": return [(move(pos, "E"), "E")]
            case "S": return [(move(pos, "W"), "W")]
    elif sym == "\\":
        match d:
            case "W": return [(move(pos, "N"), "N")]
            case "E": return [(move(pos, "S"), "S")]
            case "N": return [(move(pos, "W"), "W")]
            case "S": return [(move(pos, "E"), "E")]
    else:
        print("INVALID SYMBOL", sym)
        exit()
        
    # TODO
    return [((0,0), "N")]

V = set()

def get_lit(i_state, grid):
    F = [i_state]
    V.add(i_state)
    
    current = None
    while len(F) and (current := F.pop(0)):
        new = next_steps(*current, grid)
        for n in new:
            if valid(n[0], grid) and n not in V:
                F.append(n)
                V.add(n)

get_lit(((0,0), "E"), lines)

def count(vis):
    locs = set(map(lambda v : v[0], vis))
    return len(locs)

locs = set(map(lambda v : v[0], V))
for y in range(len(lines)):
    for x in range(len(lines[0])):
        #print(energy[y][x],end="")
        if (x, y) in locs:
            print("#", end="")
        else:
            print(lines[y][x], end="")

    print()

print(count(V))





