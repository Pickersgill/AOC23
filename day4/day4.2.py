import re

src = "./day4_input.txt"

lines = []
with open(src) as content:
    lines = list([s.strip() for s in content.readlines()])

total = 0
expr = r"(Card +\d+: +)([\d ]+)\| ([\d ]+)"

def count_card(l):
    m = re.match(expr, l)
    lefts = [int(n) for n in m[2].split()]
    rights = [int(n) for n in m[3].split()]

    copies = 0
    for l in lefts:
        if l in rights:
            copies += 1
    return copies
    #for n in range(1, copies+1):
     #   copies += count_card(i+n)

    #return copies

counts = [count_card(card) for card in lines]

def count_sum(i):
    c = 1
    for d in range(1, counts[i]+1):
        c += count_sum(i+d)
    return c

print(*counts)

total_counts = 0

for i in range(len(lines)):
    total_counts += count_sum(i)

print(total_counts)

