
src = "./day6_input.txt"


with open(src) as data:
    times, data = [l.split() for l in data.readlines()]
    time = int("".join(times[1:]))
    record = int("".join(data[1:]))
    records = [(time, record)]

print(records)

def get_time(hold, limit):
    dist = 0
    return hold * (limit-hold)


total = 1
for time, record in records:
    record_breakers = 0
    for i in range(0, time):
        t = get_time(i, time)
        if t > record:
            record_breakers += 1

    total *= record_breakers

print(total)
