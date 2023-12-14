import numpy as np

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

loaded = [
"OOOO.#.O..",
"OO..#....#",
"OO..O##..O",
"O..#.OO...",
"........#.",
"..#....#.#",
"..O..#.O.O",
"..O.......",
"#....###..",
"#....#....",
]

with open(src) as data:
    grid = np.array([list(l.strip()) for l in data.readlines()])
    #grid = np.array([list(l.strip()) for l in test])
    loaded = np.array([list(l.strip()) for l in loaded])


def load(grid):
    l = 0
    for i,row in enumerate(grid):
        for rock in row:
            if rock == "O":
                l+=grid.shape[0]-i
    return l

def tilt(grid):
    ng = np.zeros(grid.shape).astype(str)
    for col in range(grid.shape[1]):
        current_col = grid[:,col]
        for pos,rock in enumerate(current_col):
            if rock == "O":
                roll_pos = pos
                while roll_pos > 0 and current_col[roll_pos-1] == ".":
                    current_col[roll_pos] = "."
                    roll_pos -= 1
                    current_col[roll_pos] = "O"

        ng[:,col] = current_col
    return ng

                

ng = tilt(grid)
print(load(grid))
