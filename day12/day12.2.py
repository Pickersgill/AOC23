import re

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
    lines = list([(l, list([int(x) for x in g.split(",")])) for l, g in lines])
    
    #for i, l in enumerate(lines):
        #for j in range(4):
            #lines[i] = [lines[i][0] +"?"+ lines[i][0], lines[i][1] + lines[i][1]]

expr = r"#+"

def validate(line, groups):    
    i = 0
    g = groups[:]

    while i < len(line) and line[i] != "?":
        if line[i] == "#":
            if len(g) == 0:
                return True, True
            count = g.pop(0)
            check = 0
            while i < len(line) and line[i] not in "?.":
                i += 1
                check += 1
            if count > check:
                return True, False
            elif count < check:
                return True, True
        else:
            i += 1

    i -= 1
    
    #if not back:
        #b_soft, b_hard = validate(line, groups, True)
        #print(b_soft, b_hard)

    if "?" not in line and len(g) == 0:
        return False, False
    elif len(line) - i < sum(g) + len(g) - 1:
        return True, True
    else:
        return True, False

visits = 0

def combos(line, groups):
    global visits
    visits += 1
    soft, hard = validate(line, groups)
    if not (soft or hard):
        return 1
    
    if "?" not in line or hard:
        return 0

    l1 = line.replace("?", ".", 1)
    l2 = line.replace("?", "#", 1)

    c1 = combos(l1, groups)
    c2 = combos(l2, groups)
    return c1 + c2

total = 0

for l in lines:
    c = combos(*l)
    total += c

print(total)
print("TOTAL CALLS: ", visits)

