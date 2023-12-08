import re
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
print(node_map[current])

while current != "ZZZ":
    current = node_map[current][0 if lr[steps%len(lr)] == "L" else 1]
    print(current)
    steps += 1

print(current)
print(steps)
