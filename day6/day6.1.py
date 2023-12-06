
src = "./day6_input.txt"


with open(src) as data:
    times, data = [l.split() for l in data.readlines()]
    records = [(int(a), int(b)) for a, b in zip(times[1:], data[1:])]

print(records)
