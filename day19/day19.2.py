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

t2 = [
"in{a>2000:one,A}",
"one{m<1000:R,A}",
""
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
    #lines = [l.strip() for l in t2]
    
    while lines[i]:
        i += 1
    t_lines = lines[:i]

    tests = {m[1]: [Rule(x) for x in m[2].split(",")] for m in [re.match(expr, l) for l in t_lines]}

t = 0
init_part = {"x": (1,4000), "m": (1,4000), "a": (1,4000), "s": (1,4000)}

def get_combs(part):
    x = (part["x"][1]-part["x"][0])+1
    m = (part["m"][1]-part["m"][0])+1
    a = (part["a"][1]-part["a"][0])+1
    s = (part["s"][1]-part["s"][0])+1

    return x*m*a*s

def accepted(part, curr, i):
    if curr == "R":
        return 0
    elif curr == "A":
        return get_combs(part)

    def split(c, a, v):
        acc_set = part.copy()
        dec_set = part.copy()
        if c == ">":
            dec_set[a] = (acc_set[a][0], v)
            acc_set[a] = (v+1, acc_set[a][1])
        else:
            acc_set[a] = (acc_set[a][0], v-1)
            dec_set[a] = (v, dec_set[a][1])

        if acc_set[a][0] > acc_set[a][1]:
            acc_set = False
            print("HANDLE")

        if dec_set[a][0] > dec_set[a][1]:
            dec_set = False
            print("HANDLE")

        return acc_set, dec_set

    test = tests[curr][i]

    if test.default:
        return accepted(part, test.next, 0)
    else:
        acc, dec = split(test.test_comp, test.test_attr, test.test_val)
        ans1 = 0
        ans2 = 0
        if acc:
            ans1 = accepted(acc, test.next, 0)
            
        if dec:
            ans2 = accepted(dec, curr, i+1)

        return ans1+ans2

t = accepted(init_part, "in", 0)
ans = 167409079868000
print(t)
print(ans, f"{int(ans!=t)*'IN'}CORRECT")












