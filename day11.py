def solve(input: str, expansion: int) -> int:
    grid = input.split()
    galaxy_row = [False for _ in range(len(grid))]
    galaxy_col = [False for _ in range(len(grid[0]))]

    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == '#':
                galaxy_row[i] = True
                galaxy_col[j] = True
    
    galaxies = []

    expand_row = 0
    for i, row in enumerate(grid):
        expand_col = 0
        for j, c in enumerate(row):
            if c == '#':
                galaxies.append((i + expand_row, j + expand_col))
            if not galaxy_col[j]:
                expand_col += expansion
        if not galaxy_row[i]:
            expand_row += expansion

    d = 0
    for a in range(len(galaxies)):
        for b in range(a, len(galaxies)):    
            d += abs(galaxies[a][0] - galaxies[b][0]) + abs(galaxies[a][1] - galaxies[b][1])

    return d

def part_a(input: str):
    return solve(input, 1)

def part_b(input: str):
    return solve(input, 1_000_000 - 1)