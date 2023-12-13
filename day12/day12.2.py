import re
from functools import cache

src = "./day12_input.txt"

lines = []

test = [
"???.### 1,1,3", 
".??..??...?##. 1,1,3", 
"?#?#?#?#?#?#?#? 1,3,1,6", 
"????.#...#... 4,1,1", 
"????.######..#####. 1,6,5", 
"?###???????? 3,2,1", 
]

with open(src) as data:
    lines = list([[s for s in tuple(l.strip().split(" "))] for l in data.readlines()])
    #lines = list([[s for s in tuple(l.strip().split(" "))] for l in test])
    lines = list([(l, tuple([int(x) for x in g.split(",")])) for l, g in lines])
    og_lines = lines[:]
    
    for i, l in enumerate(lines):
        l = lines[i][0]
        g = lines[i][1]
        for j in range(4):
            lines[i] = [lines[i][0] + "?" + l, lines[i][1] + g]

@cache
def combos(line, groups):
    if len(groups) == 0:
        if "#" not in line:
            return 1
        else:
            return 0 

    if len(line) == 0:
        return 0
    
    def dot():
        return combos(line[1:], groups)

    def spring():
        block = line[:groups[0]]
        block = block.replace("?", "#")
        if "." in block or len(block) != groups[0]:
            return 0

        if len(line) == groups[0]:
            if len(groups) == 1:
                return 1
            else:
                return 0

        if line[groups[0]] in ".?":
            return combos(line[groups[0]+1:], groups[1:])

        return 0

    if line[0] == "#":
        return spring()
    elif line[0] == ".":
        return dot()
    else:
        return spring() + dot()
    
total = 0
for g in lines:
    total += combos(*g)
print(total)


