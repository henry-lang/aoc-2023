from itertools import cycle
from math import lcm

def parse_node(node: str):
    name, sides = node.split(' = (')
    sides = sides.split(', ')
    sides[1] = sides[1][:-1]
    return name, sides

def parse_input(input: str):
    plan, net = input.split('\n\n')
    net = dict(map(parse_node, net.split('\n')))
    return plan, net

def part_a(input: str):
    plan, net = parse_input(input)
    cur = 'AAA'
    steps = 0
    plan_iter = cycle(plan)
    while cur != 'ZZZ':
        dir = next(plan_iter)
        if dir == 'L':
            cur = net[cur][0]
        else:
            cur = net[cur][1]
        steps += 1
    
    return steps

def part_b(input: str):
    plan, net = parse_input(input)
    a = []
    for k in net:
        if k[-1] == 'A':
            a.append(k)
    a_cycle = []
    for k in a:
        cur = k
        steps = 0
        plan_iter = cycle(plan)
        while cur[-1] != 'Z':
            dir = next(plan_iter)
            if dir == 'L':
                cur = net[cur][0]
            else:
                cur = net[cur][1]
            steps += 1
        a_cycle.append(steps)
    return lcm(*a_cycle)