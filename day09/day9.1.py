
lines = []
src = "./day9_input.txt"

with open(src) as data:
    lines = list([[int(x) for x in l.strip().split()] for l in data.readlines()])


def get_next(seq):
    diffs = list([seq[i] - seq[i-1] if i > 0 else 0 for i in range(len(seq))])[1:]
    if sum(diffs) == 0:
        print("COMPLETE")
        return seq[-1]
    else:
        return seq[-1] + get_next(diffs)
    

t = 0
for seq in lines:
    t += get_next(seq)

print(t)
