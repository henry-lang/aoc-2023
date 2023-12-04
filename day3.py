from collections import defaultdict


def part_a(input: str):
    lines = [x for x in input.split("\n")]
    total = 0
    for i, l in enumerate(lines):
        j = 0
        while j < len(l):
            if l[j].isdigit():
                start = j
                sym = False
                while j < len(l) - 1 and l[j + 1].isdigit():
                    j += 1
                for cj in range(start, j + 1):
                    for di in range(i - 1, i + 2):
                        for dj in range(cj - 1, cj + 2):
                            if (
                                0 <= di < len(lines)
                                and 0 <= dj < len(l)
                                and lines[di][dj]
                                in [
                                    "@",
                                    "#",
                                    "$",
                                    "%",
                                    "^",
                                    "&",
                                    "*",
                                    "-",
                                    "+",
                                    "=",
                                    "/",
                                ]
                            ):
                                sym = True
                if sym:
                    num = int(l[start : j + 1])
                    total += num
            j += 1

    return total


def part_b(input: str):
    lines = [x for x in input.split("\n")]
    total = 0

    gear = defaultdict(list)
    for i, l in enumerate(lines):
        j = 0
        while j < len(l):
            if l[j].isdigit():
                start = j
                while j < len(l) - 1 and l[j + 1].isdigit():
                    j += 1
                num = int(l[start : j + 1])
                found = set()
                for cj in range(start, j + 1):
                    for di in range(i - 1, i + 2):
                        for dj in range(cj - 1, cj + 2):
                            if (
                                0 <= di < len(lines)
                                and 0 <= dj < len(l)
                                and lines[di][dj] == "*"
                            ):
                                if (di, dj) not in found:
                                    found.add((di, dj))
                                    gear[(di, dj)].append(num)
            j += 1

    for g in gear.values():
        if len(g) == 2:
            total += g[0] * g[1]
    return total
