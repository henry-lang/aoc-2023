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


# grid, (start r, start c)
def parse(input: str) -> tuple[list[str], tuple[int, int]]:
    grid = input.split("\n")
    sr = None
    sc = None
    for r, l in enumerate(grid):
        for c, ch in enumerate(l):
            if ch == "S":
                sr, sc = r, c
                break

    return grid, (sr, sc)


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
    grid, (sr, sc) = parse(input)

    length = tube_length(grid, sr, sc)
    return length // 2


def part_b(input: str):
    grid, (sr, sc) = parse(input)

    visited = set()
    tube_length(grid, sr, sc, visited=visited)

    crossings = [[] for _ in range(len(grid))]
    for r in range(len(grid)):
        crossings[r].append(0)
        for c in range(1, len(grid[r])):
            crossings[r].append(
                crossings[r][c - 1]
                + int(
                    (r, c - 1) in visited
                    and grid[r][c - 1] in ["S", "F", "7", "|"]
                )
            )

    total = 0
    for i, r in enumerate(crossings):
        for j, c in enumerate(r):
            if (i, j) in visited:
                continue
            if c % 2 == 1:
                total += 1

    return total
