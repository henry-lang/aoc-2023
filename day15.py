from collections import defaultdict


def hash_str(label: str):
    n = 0
    for c in label:
        ascii = ord(c)
        n += ascii
        n *= 17
        n %= 256

    return n


def part_a(input: str):
    codes = input.split(",")
    total = 0

    for code in codes:
        total += hash_str(code)
    return total


# position, focal length
Lens = tuple[int, int]


class Box:
    next_pos: int
    lenses: dict[str, Lens]

    def __init__(self):
        self.next_pos = 0
        self.lenses = {}

    def insert(self, label: str, focal: int):
        if label in self.lenses:
            self.lenses[label] = (self.lenses[label][0], focal)
        else:
            self.lenses[label] = (self.next_pos, focal)
            self.next_pos += 1

    def remove(self, label: str):
        self.lenses.pop(label, 0)

    def get_ordered_lengths(self) -> list[int]:
        lenses = list(self.lenses.values())
        lenses.sort(key=lambda x: x)
        return list(map(lambda l: l[1], lenses))


def part_b(input: str):
    codes = input.split(",")
    boxes: list[Box] = [Box() for _ in range(256)]

    for code in codes:
        if code[-1] == "-":
            label = code[:-1]
            hash = hash_str(label)
            boxes[hash].remove(label)
        else:
            label, focal = code.split("=")

            hash = hash_str(label)
            boxes[hash].insert(label, int(focal))

    total = 0
    for i, b in enumerate(boxes):
        lengths = b.get_ordered_lengths()
        for p, l in enumerate(lengths):
            total += (i + 1) * (p + 1) * l

    return total
