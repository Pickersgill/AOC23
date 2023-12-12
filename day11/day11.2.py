import numpy as np

lines = []

src = "./day11_input.txt"

test = [
"...#......",
".......#..",
"#.........",
"..........",
"......#...",
".#........",
".........#",
"..........",
".......#..",
"#...#.....",
]

with open(src) as data:
    lines = [list(l.strip()) for l in data.readlines()]
    #lines = [list(l.strip()) for l in test]

lines = np.array(lines)
stars = lines == "."

W, H = lines.shape

def get_empty(size):
    return np.array(["." for _ in range(size)])
    
rows = 0
cols = 0

e_rows = []
e_cols = []

for y in range(W):
    if np.all(stars[y]):
        print("Starless Row", y)
        e_rows.append(y)
    if np.all(stars.T[y]):
        print("Starless Col", y)
        e_cols.append(y)

star_set = set()
for y in range(W):
    for x in range(H):
        if lines[y][x] == "#":
            star_set.add((x, y))

total = 0
coef = 1000000

for star1 in star_set:
    print(star1)
    for star2 in star_set:
        if star1 != star2:
            dist = abs(star1[0]-star2[0]) + abs(star1[1]-star2[1])
            sx = min(star1[1],star2[1])
            ex = max(star1[1],star2[1])
            sy = min(star1[0],star2[0])
            ey = max(star1[0],star2[0])
            row_gaps = len(list(filter(lambda x : x in e_rows, range(sx,ex))))
            col_gaps = len(list(filter(lambda x : x in e_cols, range(sy,ey))))
            dist += (coef*row_gaps) - row_gaps
            dist += (coef*col_gaps) - col_gaps
            print("D: ", dist, star2)
            total += dist

print(total / 2)
