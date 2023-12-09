def solve(input: str, rev: bool) -> int:
    lines = [[int(n) for n in l.split()] for l in input.split('\n')]
    total = 0
    for l in lines:
        if rev:
            l = l[::-1]
        pred = l[-1]
        arr = l
        while not all(x == 0 for x in arr):
            new = []
            for i, j in zip(arr[0:], arr[1:]):
                new.append(j - i)
            arr = new
            pred += new[-1]
        total += pred
    return total

def part_a(input: str):
    return solve(input, False)

def part_b(input: str):
    return solve(input, True)