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
        for j in range(2):
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

def combos(line, groups, li=0, gi=0):
    init_li = li
    init_gi = gi
    if (li, gi) in cache.keys():
        print("CACHE")
        return cache[(li, gi)]

    li = 0
    while True:
        if li >= len(line):
            val = 1 if validate(line, groups) else 0
            cache[(li,gi)] = val
            return val
        if line[li] == "?":
            break
        li += 1
    
    l1 = line[:li] + "." + line[li+1:]
    l2 = line[:li] + "#" + line[li+1:]
    g1 = pop_groups(l1[:li+1], groups)
    g2 = pop_groups(l2[:li+1], groups)
    v1 = combos(l1, groups, li, g1)
    v2 = combos(l2, groups, li, g2)

    # CACHING NOT WORKING.    
    cache[(init_li,init_gi)] = v1 + v2
    return v1 + v2

total = 0
#print(og_lines[0], combos(*og_lines[0]))
#print(lines[0])
#print(combos(*lines[3]))
for g in [lines[0], lines[3]]:
    cache = {}
    print(g)
    print(combos(*g))
exit()


print(total)
print(v)


