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
"""
PART 2, FINDING GEARS
Since gears CAN overlap (i.e. a number may be part of two "gear systems")
We can probably find gears first, then validate them.
Given the position of a gear how do we determine it's validity...
    - Maximum number size is 3 digits, so we could find a 7x3 "neighbourhood" around the gear, search it for numbers and check their adjacency.
    - Begin by finding all numbers and recording the sets of points they occupy, for each gear parse these records for pairs of adjacent numbers

"""

def get_gear_neighbours(x, y, nums):
    num_set = []
    for dx, dy in OFFSETS:
        for n in nums:
            if (dx+x, dy+y) in n.points and n not in num_set:
                num_set.append(n)

    return num_set

total = 0

class Num:
    def __init__(self, y, re_match):
        self.m = re_match # FOR EQUALITY TESTING
        self.value = int(re_match[0])
        self.points = list(zip(range(re_match.start(), re_match.end()), [y]*len(re_match[0])))

    def __str__(self):
        return f"{self.value} spanning {self.points}"

    def __eq__(self, other):
        return self.m == other.m

nums = []
for i, row in enumerate(plans):
    nums += [Num(i, m) for m in re.finditer(r"\d+", row)]

for i, row in enumerate(plans):
    gears = re.finditer(r"\*", row)
    for g in gears:
        neighbours = get_gear_neighbours(g.start(), i, nums)

        if len(neighbours) >= 2:
            print("GEAR FOUND, BETWEEN",*neighbours)
            total += neighbours[0].value * neighbours[1].value



print(total)



