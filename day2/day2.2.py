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
    red_max = 0
    blue_max = 0
    green_max = 0
    for t in turns:
        m2 = re.findall(colour_expr, t)
        for m in m2:
            colour = m[1]
            num = int(m[0])
            match colour:
                case "green":
                    green_max = max(num, green_max)
                case "red":
                    red_max = max(num, red_max)
                case "blue":
                    blue_max = max(num, blue_max)

    total += (red_max * blue_max * green_max)

print(total)
