from heapq import heappop, heappush
from collections import defaultdict
from math import inf

src = "./day17_input.txt"
test = [
"2413432311323",
"3215453535623",
"3255245654254",
"3446585845452",
"4546657867536",
"1438598798454",
"4457876987766",
"3637877979653",
"4654967986887",
"4564679986453",
"1224686865563",
"2546548887735",
"4322674655533",
]

with open(src) as data:
    weights = [[int(x) for x in l.strip()] for l in data.readlines()]
    #weights = [[int(x) for x in l.strip()] for l in test]
    H, W = len(weights), len(weights[0])


"""
Day 17, Djikstras

- Initialize heap as left pointing and right pointing 0,0
- Expand by finding all points to min-max left and right

"""
heap = [(0, ((0, 0), (0, 1))), (0, ((0, 0), (1, 0)))]
dists = defaultdict(lambda : inf)
dest = (W-1,H-1)

lo, hi = 4, 10

while heap:
    cost, (pos, d) = heappop(heap)
    if pos == dest:
        print(cost)
        exit()
    
    dx, dy = d
    x, y = pos
    for cdx, cdy in [(-dy, dx),(dy, -dx)]:
        dcost = cost
        for i in range(1, hi+1):
            newx = x + i * cdx
            newy = y + i * cdy
            if 0 <= newx < W and 0 <= newy < H:
                dcost += weights[newy][newx]
                if i >= lo:
                    state = ((newx, newy),(cdx,cdy))
                    if dcost < dists[state]:
                        dists[state] = dcost
                        heappush(heap, (dcost, state))

        


