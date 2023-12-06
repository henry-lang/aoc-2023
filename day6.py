def part_a(input: str):
    times, distances = map(lambda l: [int(x) for x in l.split()[1:]], input.split('\n'))
    runs = list(zip(times, distances))
    # let w be wait time
    # (w * (t - w)) > d
    # wt - w^2 > d
    # wt - w^2 - d > 0

    total = 1
    for t, d in runs:
        ways = 0
        for w in range(t):
            if w * (t - w) > d:
                ways += 1
        total *= ways
        
    return total

# stupid brute force that takes 4 seconds on cpython
# didn't need to do any quadratic formula bs lol
def part_b(input: str):
    t, d = map(lambda l: int("".join(l.split()[1:])), input.split('\n'))
    
    # let w be wait time
    # (w * (t - w)) > d
    # wt - w^2 > d
    # wt - w^2 - d > 0

    ways = 0
    for w in range(t):
        if w * (t - w) > d:
            ways += 1
        
    return ways