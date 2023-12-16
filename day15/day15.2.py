src = "./day15_input.txt"
test = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
with open(src) as data:
    entries = data.read().strip().split(",")
    #entries = test.strip().split(",")

def get_val(e):
    v = 0
    for char in e:
        v += ord(char)
        v *= 17
        v = v % 256
    return v

def remove(label, boxs):
    v = get_val(label)
    if v not in boxs:
        boxs[v] = []
    else:
        old_len = len(boxs[v])
        boxs[v] = list(filter(lambda x : x[0] != label, boxs[v]))
        assert len(boxs[v]) - old_len < 2
    return boxs

def add(label, fl, boxs):
    v = get_val(label)
    if v not in boxs:
        boxs[v] = [(label, fl)]
    else:
        i = 0
        for lens in boxs[v]:
            if lens[0] == label:
                break
            i+=1
        boxs[v] = boxs[v][:i] + [(label, fl)] + boxs[v][i+1:]


    return boxs

"""
Focal lengths 1 to 9
Calc hash to indicate box we're working on
Read op symbol - or = to determine action

removal op "-":
    - find indicated box and remove lense with current label
    - could be multiple? FLAG FOR THIS
    - shift the remaining lens ???

add op "=":
    - find indicated box and replace lens with current label
    - otherwise append the lens

"""
def pretty(boxs):
    for b in boxs:
        print(f"Box {b}: {repr(boxs[b])}")
    print()

def total(boxs):
    t = 0
    """
    One plus the box number of the lens in question.
    The slot number of the lens within the box: 1 for the first lens, 2 for the second lens, and so on.
    The focal length of the lens.
    """
    for b in ([b for b in boxs if len(boxs[b]) > 0]):
        for i, (lab, fl) in enumerate(boxs[b]):
            t += (b+1) * (i+1) * int(fl)
    return t

boxs = {}
for entry in entries:
    if entry[-1] == "-":
        op = tuple("-")
        label = entry[:-1]
    else:
        op = tuple(entry[-2:])
        assert len(op) == 2
        label = entry[:-2]

    if op[0] == "-":
        boxs = remove(label, boxs)
    elif op[0] == "=":
        boxs = add(label, op[1], boxs)
    else:
        print("Something went horribly wrong...")
        exit()

print(total(boxs))
