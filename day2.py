def part_a(input: str):
    lines = input.split('\n')
    total = 0
    for i, l in enumerate(lines):
        bad = False
        take = l[l.find(':') + 2:].split('; ')
        for t in take:
            elems = t.split(', ')
            color = {'red': 0, 'green': 0, 'blue': 0}
            for e in elems:
                e = e.split()
                q = int(e[0])
                c = e[1]
                color[c] += q
            if (color['red'] > 12) or (color['green'] > 13) or (color['blue'] > 14):
                bad = True
                break
        if not bad:
            total += i + 1

    return total

def part_b(input: str):
    lines = input.split('\n')
    total = 0
    for i, l in enumerate(lines):
        take = l[l.find(':') + 2:].split('; ')
        bag = {'red': 0, 'green': 0, 'blue': 0}
        for t in take:
            elems = t.split(', ')
            color = {'red': 0, 'green': 0, 'blue': 0}
            for e in elems:
                e = e.split()
                q = int(e[0])
                c = e[1]
                color[c] += q
            bag['red'] = max(bag['red'], color['red'])
            bag['green'] = max(bag['green'], color['green'])
            bag['blue'] = max(bag['blue'], color['blue'])
        total += bag['red'] * bag['green'] * bag['blue']

    return total