def part_a(input: str):
    grid = input.split('\n')
    R = len(grid)
    C = len(grid[0])
    
    max_row = [-1] * C
    load = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '#':
                max_row[c] = r
            elif grid[r][c] == 'O':
                max_row[c] += 1
                load += C - max_row[c]
    return load

def part_b(input: str):
    grid = [list(x) for x in input.split('\n')]
    R = len(grid)
    C = len(grid[0])

    def calc_load() -> int:
        load = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 'O':
                    load += R - r
        return load
    
    for _ in range(1000):
        max_row = [-1] * C
        load = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '#':
                    max_row[c] = r
                elif grid[r][c] == 'O':
                    max_row[c] += 1
                    grid[r][c] = '.'
                    grid[max_row[c]][c] = 'O'
        
        max_col = [-1] * R
        for c in range(C):
            for r in range(R):
                if grid[r][c] == '#':
                    max_col[r] = c
                elif grid[r][c] == 'O':
                    max_col[r] += 1
                    grid[r][c] = '.'
                    grid[r][max_col[r]] = 'O'
            
        min_row = [R] * C
        for r in reversed(range(R)):
            for c in range(C):
                if grid[r][c] == '#':
                    min_row[c] = r
                elif grid[r][c] == 'O':
                    min_row[c] -= 1
                    grid[r][c] = '.'
                    grid[min_row[c]][c] = 'O'
        
        min_col = [C] * R
        for c in reversed(range(C)):
            for r in range(R):
                if grid[r][c] == '#':
                    min_col[r] = c
                elif grid[r][c] == 'O':
                    min_col[r] -= 1
                    grid[r][c] = '.'
                    grid[r][min_col[r]] = 'O'

    return calc_load()