import re

lines = []
with open("./day1_input.txt") as src:
    lines = list([l.strip() for l in src.readlines()])

word_to_num = {"one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine": "9", \
        "1" : "1", "2" : "2", "3": "3", "4" : "4", "5" : "5", "6" : "6", "7" : "7", "8" : "8", "9" : "9"}
expr = r"|".join([f"{x}" for x in word_to_num.keys()])
expr = f"(?=({expr}))" # use lookahead match with capture group to match overlapping strings without consuming string


total = 0
for l in lines:

    matches = re.finditer(expr, l)
    words = [m.group(1) for m in matches]

    s = word_to_num[words[0]] + word_to_num[words[-1]]
    total += int(s)
    #print(f"From [{l}] extracted: {int(s)}")

print("PART 2 ANSWER: ", total)



