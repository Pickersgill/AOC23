import re
src = "day19_input.txt"


with open(src) as data:
    tests = []
    lines = data.readlines()
    i = 0
    expr = r"([a-z]+){(([xmas][<>]\d+:[a-zA-Z]),?|([a-zA-Z]),?)+}"
    while (l := lines[i].strip()):
        grps = re.match(expr, l)
        print(l)
        for g in grps.groups():
            print(g)
        tests.append(grps[1])
        i += 1

    i += 1

