from itertools import groupby

def parse(input: str) -> tuple[list[int], list[list[list[int]]]]:
    seeds, *maps = input.split('\n')
    seeds = [int(x) for x in seeds.split()[1:]]
    maps = [[[int(v) for v in x.split()] for x in list(sub)[1:]] for ele, sub in groupby(maps, key = bool) if ele]

    return seeds, maps

def part_a(input: str):
    seeds, maps = parse(input)
    
    ans = 10**10
    for s in seeds:
        value = s
        for m in maps:
            print(s, value)
            for dst, src, range in m:
                if src<=value<(src+range):
                    print(src, value, src+range)
                    value = dst + (value - src)
                    break
        ans = min(ans, value)

    return ans

def part_b(input: str):
    seeds, maps = parse(input)
    

