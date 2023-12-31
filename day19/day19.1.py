import re
src = "day19_input.txt"

test = [
"px{a<2006:qkq,m>2090:A,rfg}",
"pv{a>1716:R,A}",
"lnx{m>1548:A,A}",
"rfg{s<537:gd,x>2440:R,A}",
"qs{s>3448:A,lnx}",
"qkq{x<1416:A,crn}",
"crn{x>2662:A,R}",
"in{s<1351:px,qqz}",
"qqz{s>2770:qs,m<1801:hdj,R}",
"gd{a>3333:R,R}",
"hdj{m>838:A,pv}",
"",
"{x=787,m=2655,a=1222,s=2876}",
"{x=1679,m=44,a=2067,s=496}",
"{x=2036,m=264,a=79,s=2244}",
"{x=2461,m=1339,a=466,s=291}",
"{x=2127,m=1623,a=2188,s=1013}",
]

class Rule:
    def __init__(self, text):
        self.t = text
        if ":" not in text:
            self.default = True
            self.next = text
        else:
            grps = re.match(r"([xmas])([<>])(\d+):([a-zAR]+)", text)
            self.test_attr = grps[1]
            self.test_comp = grps[2]
            self.test_val = int(grps[3])
            self.next = grps[4]
            self.default = False

    def eval(self, part):
        if self.default:
            return self.next
        if self.test_comp == "<":
            return self.next if part[self.test_attr] < self.test_val else False
        elif self.test_comp == ">":
            return self.next if part[self.test_attr] > self.test_val else False
        print("BAD PART/RULE", self, part)
        

    def __str__(self):
        return self.t
    def __repr__(self):
        return str(self)

with open(src) as data:
    i = 0
    expr = r"([a-z]+){(.*)}"
    lines = [l.strip() for l in data.readlines()]
    #lines = [l.strip() for l in test]
    
    while lines[i]:
        i += 1
    t_lines = lines[:i]
    i += 1
    part_lines = lines[i:]

    tests = {m[1]: [Rule(x) for x in m[2].split(",")] for m in [re.match(expr, l) for l in t_lines]}
    parts = [{p[0] : int(p[1]) for p in re.findall(r"([xmas])=(\d+)", l)} for l in part_lines]


t = 0
for part in parts:
    curr = "in"
    while curr not in "AR":
        ts = tests[curr][:]
        res = False
        while not res:
            res = ts.pop(0).eval(part)
        curr = res
    
    if curr == "A":
        t += sum(part.values())

print(t)













