import re

lines = []

src = "./day2_input.txt"

# only 12 red cubes, 13 green cubes, and 14 blue cubes



with open(src) as f:
    lines = [s.strip() for s in f.readlines()]

expr = r"Game (\d+): (.*)"
colour_expr = r"(\d+) (green|red|blue)"

total = 0

for l in lines:
    m = re.match(expr, l)
    id = m.group(1)
    turns = m.group(2).split(";")
    excess = False
    for t in turns:
        m2 = re.findall(colour_expr, t)
        for m in m2:
            colour = m[1]
            num = int(m[0])
            match colour:
                case "green":
                    excess = excess or num > 13
                case "red":
                    excess = excess or num > 12
                case "blue":
                    excess = excess or num > 14
    if not excess:
        total += int(id)

print(total)
