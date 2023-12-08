import re
import math
src = "./day8_input.txt"

with open(src) as data:
    lines = data.readlines()
    lr = lines[0].strip()
    node_map = {}
    for line in lines[2:]:
        key, vals = line.strip().split(" = ")
        m = re.match(r"\(([A-Z]+), ([A-Z]+)\)", vals)
        node_map[key] = (m[1], m[2])

steps = 0
current = "AAA"

a_nodes = list(filter(lambda x : x[-1]=="A", node_map.keys()))

ends = []
for a in a_nodes:
    steps = 0
    current = a
    while current[-1] != "Z":
        current = node_map[current][0 if lr[steps%len(lr)] == "L" else 1]
        steps += 1
    ends += [steps]

print(current)
print(steps)
print(ends)

print(math.lcm(*ends))
