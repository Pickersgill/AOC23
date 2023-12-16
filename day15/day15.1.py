src = "./day15_input.txt"
test = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
with open(src) as data:
    entries = data.read().strip().split(",")
    #entries = test.strip().split(",")

print(entries[-10:])


def get_val(e):
    v = 0
    for char in e:
        v += ord(char)
        v *= 17
        v = v % 256
    return v

t = 0
for entry in entries:
    t += get_val(entry)

print(t)
