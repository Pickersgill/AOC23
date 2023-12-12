import numpy as np

lines = []

src = "./day11_input.txt"

test = [
    "#.........",
    ".#........",
    "..#.......",
    "...#......",
    "..........",
    ".....#....",
    "......#...",
    ".......#..",
    "........#.",
    "..........",
]

with open(src) as data:
    lines = [list(l.strip()) for l in data.readlines()]
    #lines = [list(l.strip()) for l in test]

lines = np.array(lines)
stars = lines == "."

W, H = lines.shape
print(W,H)
new_map = lines[:]

def get_empty(size):
    return np.array(["." for _ in range(size)])
    
rows = 0
cols = 0

for y in range(W):
    if np.all(stars[y]):
        print("Starless Row", y)
        new_map = np.concatenate([new_map[:y+rows], [get_empty(W+cols)], new_map[y+rows:]])
        rows += 1
    if np.all(stars.T[y]):
        print("Starless Col", y)
        new_map = np.concatenate([new_map.T[:y+cols], [get_empty(H+rows)], new_map.T[y+cols:]]).T
        cols += 1

t = [1, 2, 3, 4, 5]
print(rows, cols)
print(W, H)
print(*new_map.shape)

star_set = set()
for y in range(new_map.shape[0]):
    for x in range(new_map.shape[1]):
        if new_map[y][x] == "#":
            star_set.add((x, y))

total = 0

for star1 in star_set:
    for star2 in star_set:
        total += abs(star1[0]-star2[0]) + abs(star1[1]-star2[1])

print(total/2)
            




