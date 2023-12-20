import re
src = "day20_input.txt"

class Gate:
    """
    Flip flop, starts low, ignore high pulse, low pulse: flip and send

    Conj, rememeber each pulse, defaults low. After pulse if all high send low else send high
    """
    def __init__(self, text):
        self.t = text
        grps = re.match(r"((broadcaster)|[%&]([a-z]+)) -> (.*)", text)
        self.ctype = grps[1]
        self.outs = grps[4].split(", ")
        self.name = grps[2] if grps[2] else grps[3]
        self.ins = []
        self.mem = 0

    def add_in(self, g):
        self.ins.append((0,g))

    def pulse(self, hi):
        print(self.ctype)
        if self.ctype == "broadcaster":
            pulse = hi
        elif self.ctype == "&":
            if all([i[0]==1 for i in self.ins]):
                pulse = 0
            else:
                pulse = 1
        elif self.ctype == "%":
            if not hi:
                self.mem = 1 - self.mem
                pulse = self.mem
            else:
                return []
        else:
            print("BAD")
            pulse = -1

        return [(pulse, o) for o in self.outs]
    
    def __str__(self):
        return self.t

    def __repr__(self):
        return str(self)

with open(src) as data:
    gate_list = [Gate(l.strip()) for l in data.readlines()]
    gates = {g.name: g for g in gate_list}
    for gate in gate_list:
        for out in gate.outs:
            if out in gates.keys():
                gates[out].add_in(gate.name)
    

events = [(0, "broadcaster")]
for i in range(1000):
    n_events = []
    for hi, n in events:
        if n in gates.keys():
            n_events += gates[n].pulse(hi)

    events = n_events
    

"""
Create new pulse event
Resolve each pulse event, creating all new events,
Repeat
"""



print("DONT FORGET ABOUT WONKY RX")
