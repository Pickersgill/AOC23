import re 

# any number not mapped is reflexive

# find seed with lowest location number

src = "./day5_input.txt"
lines = []

split_expr = r"^\s*$"
with open(src) as data:
    lines = re.split(split_expr, data.read(), flags=re.M)

def lines_to_seedlist(data):
    name, data = [x.strip() for x in data.split(":")]
    data = list([int(x) for x in data.split()])
    return name, data

def lines_to_map(data):
    name, data = [x.strip() for x in data.split(":")]
    data = [row.split() for row in data.split("\n")]
    data = [(int(x), int(y), int(z)) for x, y, z in data]
    return name, data

maps = {}

name, records = lines_to_seedlist(lines[0])
maps[name] = records

for line in lines[1:]:
    if line:
        name, records = lines_to_map(line)
        maps[name] = records

def use_map(m, key):
    for d, s, r in m:
        # for each row if the key is between the source and source + range
        # return destination + key - source
        # else return key
        if key in range(s, s+r):
            return d + key - s
    return key

MAP_ORDER = list(maps.keys())[1:]

print(maps["seeds"])

min_seed = None
min_loc = None
for seed in maps["seeds"]:
    key = seed
    for m in MAP_ORDER:
        key = use_map(maps[m], key)
    
    if not min_loc or key < min_loc:
        min_loc = key
        min_seed = seed

print("Minimum Seed: ", min_seed)
print("Minimum Location: ", min_loc)

    

        
