import re
from functools import lru_cache

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
    #lines = list([[s for s in tuple(l.strip().split(" "))] for l in data.readlines()])
    lines = list([[s for s in tuple(l.strip().split(" "))] for l in test])
    lines = list([(l, list([int(x) for x in g.split(",")])) for l, g in lines])
    og_lines = lines[:]
    
    for i, l in enumerate(lines):
        l = lines[i][0]
        g = lines[i][1]
        for j in range(1):
            lines[i] = [lines[i][0] + "?" + l, lines[i][1] + g]


expr = r"#+"

def validate(line, groups):    
    if "?" in line:
        return False

    matches = re.findall(expr, line)
    if len(matches) != len(groups):
        return False

    for i in range(len(groups)):
        if len(matches[i]) != groups[i]:
            return False

    return True

v = 0

cache = {}

def pop_groups(l, gs):
    gs = gs[:]
    ms = re.findall(r"#+", l)
    count = 0
    for m in ms:
        if len(gs) > 0 and len(m) == gs.pop(0):
            count += 1
        else:
            break
    return count

@lru_cache
def combos(line, groups, li=0, gi=0):
    if gi == len(groups) and len(filter(lambda x : x == "#", line[li:])) == 0:
        return 1
    if li == len(line) and gi != len(groups):
        return 0
    
    while True:
        if line[li] == ".":
            break
        li += 1

    springs = 0
    while True:
        if springs == groups[gi]:
            break
        
    
    if line[li] == "#":
        return 0

    
    
total = 0
#print(og_lines[0], combos(*og_lines[0]))
#print(lines[0])
#print(combos(*lines[3]))
for g in [lines[0]]:
    cache = {}
    print(g, len(g[0]))
    print(combos(*g))
exit()


print(total)
print(v)


