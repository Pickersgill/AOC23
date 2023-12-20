import re
src = "day20_input.txt"

t1 = [
"broadcaster -> a, b, c",
"%a -> b",
"%b -> c",
"%c -> inv",
"&inv -> a",
]

t2 = [
"broadcaster -> a",
"%a -> inv, con",
"&inv -> b",
"%b -> con",
"&con -> output",
]
class Gate:
    """
    Flip flop, starts low, ignore high pulse, low pulse: flip and send

    Conj, rememeber each pulse, defaults low. After pulse if all high send low else send high
    """
    def __init__(self, text):
        self.t = text
        grps = re.match(r"([&%]?)(broadcaster|[a-z]+) -> (.*)", text)
        self.ctype = grps[1]
        self.outs = grps[3].split(", ")
        self.name = grps[2]
        if self.name == "broadcaster":
            self.ctype = self.name
        self.ins = {}
        self.mem = 0

    def as_dot(self):
        return "\n".join([f"{self.name} -> {o}" for o in self.outs])
    
    def add_in(self, g):
        self.ins[g] = 0

    def pulse(self, sender, hi):
        if self.ctype == "broadcaster":
            pulse = hi
        elif self.ctype == "&":
            self.ins[sender] = hi
            if all([i==1 for i in self.ins.values()]):
                pulse = 0
            else:
                pulse = 1
        elif self.ctype == "%":
            if not hi:
                self.mem = 1 - self.mem
                pulse = self.mem
            else:
                return 0, 0, []
        else:
            print("BAD")
            pulse = -1
        
        l = len(self.outs) * (1 - pulse)
        h = len(self.outs) * pulse
        return l, h, [(self.name, pulse, o) for o in self.outs]
    
    def __str__(self):
        return self.t

    def __repr__(self):
        return str(self)

with open(src) as data:
    gate_list = [Gate(l.strip()) for l in data.readlines()]
    #gate_list = [Gate(l.strip()) for l in t1]
    #gate_list = [Gate(l.strip()) for l in t2]
    gates = {g.name: g for g in gate_list}
    for gate in gate_list:
        for out in gate.outs:
            if out in gates.keys():
                gates[out].add_in(gate.name)
    

lows = 0
highs = 0
i = 0
"""
RX has one input, GF

GF is a conjunction with 4 inputs
GF will give a low pulse only when all 4 of these inputs are HI
Find the cycle size for each input
Find the LCM of these
"""
loops = {}
start_gates = gate_list[:]
test_gates = list(gates["gf"].ins.keys())
for g in test_gates:
    c = 0
    events = []
    end = False
    print(g)
    while not end:
        c += 1
        events = [("button", 0, "broadcaster")]
        while len(events) > 0:
            n_events = []
            for sender, hi, n in events:
                if n in gates.keys():
                    l, h, evs = gates[n].pulse(sender, hi)
                    n_events += evs
            events = n_events
            if (g, 1, "gf") in events:
                end = True
    print(c)
    gate_list = start_gates
