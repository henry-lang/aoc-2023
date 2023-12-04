import functools


def part_a(input: str):
    lines = input.split('\n')
    total = 0
    for l in lines:
        lhs, rhs = map(lambda s: [x for x in s.split()], l.split('|'))
        lhs = lhs[2:]
        lhs, rhs = set([int(x) for x in lhs]), [int(x) for x in rhs]
        value = 0
        for n in rhs:
            if n in lhs:
                if value == 0:
                    value = 1
                else:
                    value *= 2
        total += value
    return total

def cards_of_list(matches: list[int]):
    @functools.cache
    def cards(index: int):
        total = 1
        for i in range(matches[index]):
            total += cards(index + 1 + i)
        return total

    return cards

def part_b(input: str):
    lines = input.split('\n')
    
    matches = []

    for l in lines:
        lhs, rhs = map(lambda s: [x for x in s.split()], l.split('|'))
        lhs = lhs[2:]
        lhs, rhs = set([int(x) for x in lhs]), [int(x) for x in rhs]
        total = 0
        for n in rhs:
            if n in lhs:
                total += 1
        matches.append(total)
    
    total = 0
    cards = cards_of_list(matches)
    for i in range(len(matches)):
        total += cards(i)
    return total