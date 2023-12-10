#!/usr/bin/env python3

import argparse
from time import time

parser = argparse.ArgumentParser(prog='Advent of Code Runner')
parser.add_argument('day')
parser.add_argument('input_file')
args = parser.parse_args()

day = args.day[:-1]
part = args.day[-1]

with open(args.input_file) as file:
    solve_fn = getattr(__import__(f'day{day}'), f'part_{part}')
    contents = file.read()
    start = time()
    ans = solve_fn(contents)
    end = time()
    print(f'answer: {ans}')
    print(f'took: {round((end - start) * 1000, 2)}ms')