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
    #lines = list([[s for s in tuple(l.strip().split(" "))] for l in data.readlines()])
    lines = list([[s for s in tuple(l.strip().split(" "))] for l in test])
    lines = list([(l, list([int(x) for x in g.split(",")])) for l, g in lines])
    og_lines = lines[:]
    
    for i, l in enumerate(lines):
        l = lines[i][0]
        g = lines[i][1]
        for j in range(4):
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

def combos(line, groups, li=0, gi=0):
    if (li, gi) in cache.keys():
        return cache[(li, gi)]

    if li >= len(line):
        if validate(line, groups):
            cache[(li,gi)] = 1
            return 1
        else:
            cache[(li,gi)] = 0
            return 0
    
    #print(line, groups)
    #print(line[li:], groups[gi:])
    springs = 0
    just_popped = False
    li = 0
    gi = 0
    while True:
        if li >= len(line) or line[li] == "?":
            #print("ENDING")
            break
        just_popped = False
        #print(f"READING {line[li]} AT {li}")
        if line[li] == "#":
            springs += 1
            if springs == groups[gi]:
                #print(f"POPPING SPRING GROUP {gi} OF LEN {groups[gi]} AT {li}")
                just_popped = True
                springs = 0
                gi+=1
        elif line[li] == ".":
            springs = 0

        li += 1

    if li >= len(line) and gi != len(groups):
        #print("FAIL")
        cache[(li,gi)] = 0
        return 0

    if li < len(line):
        l2 = line[:li] + "." + line[li+1:]
        l1 = line[:li] + "#" + line[li+1:]
        if not just_popped:
            #print()
            val = combos(l1, groups, li, gi) + combos(l2, groups, li, gi)
            cache[(li,gi)] = val
            return val
        else:
            #print("ALTING")
            #print()
            val = combos(l2, groups, li, gi)
            cache[(li,gi)] = val
            return val
    else:
        if gi == len(groups):
            print("SUCCESS", line)
            cache[(li,gi)] = 1
            return 1
        else:
            cache[(li,gi)] = 0
            return 0
    

total = 0
#print(og_lines[0], combos(*og_lines[0]))
print(lines[0])
print(combos(*lines[0]))
cache = {}
print(lines[3], combos(*lines[3]))
exit()


print(total)
print(v)


