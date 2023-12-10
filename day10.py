import sys

sys.setrecursionlimit(100000)

offsets = {
    "|": [(1, 0), (-1, 0)],
    "-": [(0, 1), (0, -1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
    "S": [(1, 0), (-1, 0), (0, -1), (0, 1)],
}


def can_move_to(grid: list[str], visited: set[tuple[int, int]], r: int, c: int) -> bool:
    return (
        0 <= r < len(grid)
        and 0 <= c < len(grid[r])
        and grid[r][c] != "."
        and not (r, c) in visited
    )

def tube_length(
    grid: list[str], r: int, c: int, distance=0, visited: set = set()
) -> int:
    for dr, dc in offsets[grid[r][c]]:
        nr, nc = r + dr, c + dc
        if can_move_to(grid, visited, nr, nc):
            visited.add((nr, nc))
            return tube_length(grid, nr, nc, distance + 1, visited)
    return distance


def part_a(input: str):
    grid = input.split("\n")

    sr = None
    sc = None
    for r, l in enumerate(grid):
        for c, ch in enumerate(l):
            if ch == "S":
                sr, sc = r, c
                break

    length = tube_length(grid, sr, sc)
    return length // 2

def part_b(input: str):
    grid = input.split("\n")

    sr = None
    sc = None
    for r, l in enumerate(grid):
        for c, ch in enumerate(l):
            if ch == "S":
                sr, sc = r, c
                break

    visited = set()
    tube_length(grid, sr, sc, visited=visited)
