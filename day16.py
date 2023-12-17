from sys import setrecursionlimit

setrecursionlimit(10**6)

def num_energized(grid: list[str], r: int, c: int, vr: int, vc: int):
    R = len(grid)
    C = len(grid[0])

    visited = set()
    memo = set()

    def solve(r: int, c: int, vr: int, vc: int):
        if r < 0 or r >= R or c < 0 or c >= C:
            return
        if (r, c, vr, vc) in memo:
            return
        
        memo.add((r, c, vr, vc))
        visited.add((r, c))

        if grid[r][c] == '.':
            solve(r + vr, c + vc, vr, vc)
        elif grid[r][c] == '|':
            if vc != 0:
                solve(r - 1, c, -1, 0)
                solve(r + 1, c, 1, 0)
            else:
                solve(r + vr, c + vc, vr, vc)
        elif grid[r][c] == '-':
            if vr != 0:
                solve(r, c - 1, 0, -1)
                solve(r, c + 1, 0, 1)
            else:
                solve(r + vr, c + vc, vr, vc)
        elif grid[r][c] == '\\':
            if (vr, vc) == (1, 0):
                solve(r, c + 1, 0, 1)
            elif (vr, vc) == (-1, 0):
                solve(r, c - 1, 0, -1)
            elif (vr, vc) == (0, 1):
                solve(r + 1, c, 1, 0)
            elif (vr, vc) == (0, -1):
                solve(r - 1, c, -1, 0)
        elif grid[r][c] == '/':
            if (vr, vc) == (1, 0):
                solve(r, c - 1, 0, -1)
            elif (vr, vc) == (-1, 0):
                solve(r, c + 1, 0, 1)
            elif (vr, vc) == (0, 1):
                solve(r - 1, c, -1, 0)
            elif (vr, vc) == (0, -1):
                solve(r + 1, c, 1, 0)
    
    solve(r, c, vr, vc)
    return len(visited)

def part_a(input: str):
    grid = input.split('\n')

    return num_energized(grid, 0, 0, 0, 1)

def part_b(input: str):
    grid = input.split('\n')
    max_energized = 0

    for r in range(len(grid)):
        max_energized = max(max_energized, num_energized(grid, r, 0, 0, 1), num_energized(grid, r, len(grid[0]) - 1, 0, -1))
    
    for c in range(len(grid[0])):
        max_energized = max(max_energized, num_energized(grid, 0, c, 1, 0), num_energized(grid, len(grid) - 1, c, -1, 0))
    
    return max_energized