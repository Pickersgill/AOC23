import numpy as np

hands = []

src = "./day7_input.txt"
with open(src) as data:
    hands = [l.strip().split() for l in data.readlines()]

def score_by_hand(hand):
    hand = list(hand)
    _, counts = np.unique(hand, return_counts=True)
    counts.sort()

    match list(counts):
        case [1, 1, 1, 1, 1]:
            return 1
        case [1, 1, 1, 2]:
            return 2
        case [1, 2, 2]:
            return 3
        case [1, 1, 3]:
            return 4
        case [2, 3]:
            return 5
        case [1, 4]:
            return 6
        case [5]:
            return 7

cards = "AKQJT98765432"
scores = dict([(y, x) for x, y in enumerate(cards[::-1])])
def score_by_high(hand, ind=0):
    return scores[hand[ind]]
    
def score_combined(hand):
    hand, _ = hand
    return (
        score_by_hand(hand), 
        score_by_high(hand, 0),
        score_by_high(hand, 1),
        score_by_high(hand, 2),
        score_by_high(hand, 3),
        score_by_high(hand, 4)
    )

hands.sort(key=score_combined)
total = 0
for rank, (hand, bet) in enumerate(hands):
    print(rank+1, hand, bet)
    total += (rank+1)*int(bet)
    
print(total)


