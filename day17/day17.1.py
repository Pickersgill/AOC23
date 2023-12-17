import numpy as np

src = "./day17_input.txt"

with open(src) as data:
    weights = np.array([list(l.strip()) for l in data.readlines()]).astype(int)
    H, W = weights.shape

def move(p, d):
    match d:
        case "N": return (p[0], p[1]-1)
        case "S": return (p[0], p[1]+1)
        case "E": return (p[0]+1, p[1])
        case "W": return (p[0]-1, p[1])
        case _: 
            print("BAD", p, d)
            raise RuntimeError

# p3, the previous 3 moves
def get_neighbours(current, p3, V):
    dirs = list("NSEW")
    for d in dirs[:]:
        if p3 == d * 3:
            dirs.remove(d)

    ns = []
    for d in dirs:
        new_pos = move(current, d)
        if new_pos[0] >= 0 and new_pos[0] < W and new_pos[1] >= 0 and new_pos[1] < H and not V[new_pos[1],new_pos[0]]:
            ns.append(new_pos)

    return ns
    

"""
Day 17, Djikstras
"""
dists = np.ones(weights.shape) * np.Infinity
visits = np.zeros(weights.shape)
dists[0,0] = 0

current = (0,0)
print(weights)

while not visits[H-1,W-1]:
    ns = get_neighbours(current, "", visits)
    for nx,ny in ns:
        dists[ny,nx] = min(dists[current[1], current[0]] + weights[ny,nx], dists[ny,nx])

    visits[current[1],current[0]] = 1
    current = np.unravel_index(np.argmin((visits * np.Infinity) + dists), dists.shape)
    current = (current[1],current[0])


print(weights)
print(dists)
print(dists[H-1,W-1])

