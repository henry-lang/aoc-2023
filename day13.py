from math import log2

def part_a(input: str):
    notes = [l.split() for l in input.split('\n\n')]
    total = 0

    for n in notes:
        rows = []
        cols = []
        for row in n:
            num = 0
            for ch in row:
                num *= 2
                num += ch == '#'
            rows.append(num)
        for col in range(len(n[0])):
            num = 0
            for row in range(len(n)):
                num *= 2
                num += n[row][col] == '#'
            cols.append(num)

        for i in range(1, len(rows)):
            lhs = rows[0:i]
            rhs = rows[i:]
            if all(a == b for a, b in zip(reversed(lhs), rhs)):
                total += 100 * i
                break
        
        for i in range(1, len(cols)):
            lhs = cols[0:i]
            rhs = cols[i:]
            if all(a == b for a, b in zip(reversed(lhs), rhs)):
                total += i
                break
        
    return total

def part_b(input: str):
    notes = [l.split() for l in input.split('\n\n')]
    total = 0

    for n in notes:
        rows = []
        cols = []
        for row in n:
            num = 0
            for ch in row:
                num *= 2
                num += ch == '#'
            rows.append(num)
        for col in range(len(n[0])):
            num = 0
            for row in range(len(n)):
                num *= 2
                num += n[row][col] == '#'
            cols.append(num)

        for i in range(1, len(rows)):
            lhs = rows[0:i]
            rhs = rows[i:]
            found = False
            invalid = False
            for a, b in zip(reversed(lhs), rhs):
                if a == b:
                    continue
                elif log2(a ^ b).is_integer():
                    if found:
                        invalid = True
                        break
                    else:
                        found = True
                else:
                    invalid = True
                    break
            if found and not invalid:
                total += 100 * i

        for i in range(1, len(cols)):
            lhs = cols[0:i]
            rhs = cols[i:]
            found = False
            invalid = False
            for a, b in zip(reversed(lhs), rhs):
                if a == b:
                    continue
                elif log2(a ^ b).is_integer():
                    if found:
                        invalid = True
                        break
                    else:
                        found = True
                else:
                    invalid = True
                    break
            if found and not invalid:
                total += i
        
    return total