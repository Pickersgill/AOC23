import re

src = "./day3_input.txt"


# WHAT IS A SYMBOL?
symbol_re = r"[^\d\.]"

OFFSETS = [
        [-1, -1], [0, -1], [1, -1],
        [-1, 0],           [1, 0],
        [-1, 1], [0, 1], [1, 1]
        ]

plans = []
with open(src) as content:
    plans = list([s.strip() for s in content.readlines()])

ROWS = len(plans)
COLS = len(plans[0])
# Search the input space until we find a number (findall, use spans)
# Check for adjacency
# Add to total

def is_adj(y, start, end):
    span = end-start
    for x in range(start, end):
        for dx, dy in OFFSETS:
            if y+dy >= 0 and y+dy < ROWS and x+dx >= 0 and x+dx < COLS:
                test = plans[y+dy][x+dx]
                if re.match(symbol_re, test):
                    return True
                
    print(plans[y][start:end])
    return False

total = 0

for i, row in enumerate(plans):
    nums = re.finditer(r"\d+", row)
    for n in nums:
        val = int(n[0])
        if is_adj(i, n.start(), n.end()):
            total += val

print(total)



