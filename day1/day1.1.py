import re

lines = []
with open("./day1_input.txt") as src:
    lines = list([re.sub("[a-zA-Z]", "", l.strip()) for l in src.readlines()])

total = sum([int(l[0] + l[-1]) for l in lines])
print("PART 1 ANSWER: ", total)


