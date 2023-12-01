#!/usr/bin/env python3

from sys import argv
from time import time

arg = argv[1]
day = arg[:-1]
part = arg[-1]

in_file = argv[2]
with open(in_file) as file:
    solve_fn = getattr(__import__(f'day{day}'), f'part_{part}')
    start = time()
    solve_fn(file.read())
    end = time()
    print(f'took: {(end - start) * 1000}ms')