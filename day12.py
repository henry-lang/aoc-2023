def part_a(input: str):
    lines = input.split('\n')
    
    for l in lines:
        spring, counts = l.split(' ')
        counts = [int(x) for x in counts.split(',')]
        old = [0 for _ in range(len(spring) + 1)]
        new = [int(s == '#') for s in spring] + [0]
        for count in counts:
            found = 0
            for i, c in enumerate(spring):
                if c == '.':
                    found += 1
                if c == '#':
                    new[i + 1] += new[i]
                if found >= count and spring[i - count] != '#':
                    new[i + 1] -= old[i - count]
            for i in range(len(old)):
                old[i] = 0
            new, old = old, new
            print(new, old)