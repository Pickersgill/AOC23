
lines = []
src = "./day9_input.txt"

with open(src) as data:
    lines = list([[int(x) for x in l.strip().split()] for l in data.readlines()])


def get_first(seq):
    diffs = list([seq[i] - seq[i-1] if i > 0 else 0 for i in range(len(seq))])[1:]
    # first elem in seq
    # MINUS first elem in diffs
    if sum(diffs) == 0:
        print("COMPLETE")
        return seq[0]
    else:
        return seq[0] - get_first(diffs)
    

t = 0
test = [10,13,16,21,30,45]
print(get_first(test))

for s in lines:
    t+=get_first(s)

print(t)
