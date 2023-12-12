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
def combos(line, groups):
    global v
    v += 1
    if validate(line, groups):
        return 1
    
    if "?" not in line:
        return 0

    l1 = line.replace("?", ".", 1)
    l2 = line.replace("?", "#", 1)

    c1 = combos(l1, groups)
    c2 = combos(l2, groups)
    return c1 + c2

total = 0
print(og_lines[0], combos(*og_lines[0]))
print(lines[0], combos(*lines[0]))
print(og_lines[3], combos(*og_lines[3]))
print(lines[3], combos(*lines[3]))

exit()

print(total)
print(v)


