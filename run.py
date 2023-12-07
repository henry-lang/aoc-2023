#!/usr/bin/env python3

from sys import argv
from time import time

arg = argv[1]
day = arg[:-1]
part = arg[-1]

in_file = argv[2]
with open(in_file) as file:
    solve_fn = getattr(__import__(f'day{day}'), f'part_{part}')
    contents = file.read()
    start = time()
    ans = solve_fn(contents)
    end = time()
    print(f'answer: {ans}')
    print(f'took: {round((end - start) * 1000, 2)}ms')