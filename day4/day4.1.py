import re

src = "./day4_input.txt"

lines = []
with open(src) as content:
    lines = list([s.strip() for s in content.readlines()])

total = 0
expr = r"(Card +\d+: +)([\d ]+)\| ([\d ]+)"

for l in lines:
    m = re.match(expr, l)
    lefts = [int(n) for n in m[2].split()]
    rights = [int(n) for n in m[3].split()]

    t = 0
    for l in lefts:
        if l in rights:
            if t == 0:
                t = 1
            else:
                t *= 2
    total += t

print(total)
