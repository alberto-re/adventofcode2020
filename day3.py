#!/usr/bin/env python3
# --- Day 3: Toboggan Trajectory ---

from functools import reduce

lines = []
with open("input/day3.txt") as f:
    lines = [[c for c in line.rstrip()] for line in f]


def traverse(area_map, stepx, stepy):
    x, y, trees = 0, 0, 0
    while True:
        x += stepx
        x %= len(lines[0])
        y += stepy
        if y >= len(lines):
            break
        if lines[y][x] == "#":
            trees += 1
    return trees


print("part1 solution:", traverse(lines, 3, 1))

slopes = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2],
]
print(
    "part2 solution:",
    reduce(
        lambda x, y: x * y, [traverse(lines, slope[0], slope[1]) for slope in slopes]
    ),
)
