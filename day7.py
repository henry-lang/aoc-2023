from collections import defaultdict

value_a = dict(zip(['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'], range(13)))
value_b = dict(zip(['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A'], range(13)))

def part_a(input: str):
    total = 0
    lines = input.split('\n')
    ranks = []
    for l in lines:
        hand, bet = l.split()
        bet = int(bet)
        freqs = defaultdict(int)
        for c in hand:
            freqs[c] += 1
        freqs = sorted(list(freqs.items()), key=lambda c: c[1], reverse=True)
        power = None
        if len(freqs) == 1:
            power = 7
        elif len(freqs) == 2:
            if freqs[0][1] == 4:
                power = 6
            else:
                # full house
                power = 5
        elif len(freqs) == 3:
            if freqs[0][1] == 3:
                power = 4
            elif freqs[0][1] == 2:
                power = 3
        elif len(freqs) == 4:
            power = 2
        elif len(freqs) == 5:
            power = 1
        ranks.append((power, tuple(map(lambda c: value_a[c], hand)), bet))
    ranks.sort(key=lambda r: (r[0], r[1]))
    for i, r in enumerate(ranks):
        total += (i + 1) * r[2]
    return total

def part_b(input: str):
    total = 0
    lines = input.split('\n')
    ranks = []
    for l in lines:
        hand, bet = l.split()
        bet = int(bet)
        freq_set = defaultdict(int)
        for c in hand:
            freq_set[c] += 1
        freqs = sorted(list(freq_set.items()), key=lambda c: c[1], reverse=True)
        if 'J' in freq_set and len(freq_set) > 1:
            index = next(i for i, x in enumerate(freqs) if x[0] == 'J')
            freqs.pop(index)
            freqs[0] = (freqs[0][0], freqs[0][1] + freq_set['J'])

        power = None
        if len(freqs) == 1:
            power = 7
        elif len(freqs) == 2:
            if freqs[0][1] == 4:
                power = 6
            else:
                # full house
                power = 5
        elif len(freqs) == 3:
            if freqs[0][1] == 3:
                power = 4
            elif freqs[0][1] == 2:
                power = 3
        elif len(freqs) == 4:
            power = 2
        elif len(freqs) == 5:
            power = 1
        ranks.append((power, tuple(map(lambda c: value_b[c], hand)), bet))
    ranks.sort(key=lambda r: (r[0], r[1]))
    for i, r in enumerate(ranks):
        total += (i + 1) * r[2]
    return total
            