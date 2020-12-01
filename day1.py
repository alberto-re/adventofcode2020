#!/usr/bin/env python3
# --- Day 1: Report Repair ---

from functools import reduce

def entriesThatSum(n, m, array, exclude=[]):
    """Given an ordered array of numbers returns the m entries that sum to n, if any.

    This code assumes there is no more than m entries that satisfies the condition
    in the input list. In case there are more only the first one is returned.
    """
    assert m >= 2
    assert len(array) <= n

    if m == 2:
        for i in range(len(array)):
            if i in exclude:
                continue
            for j in range(len(array) - 1, 0, -1):
                if j in exclude:
                    continue
                if array[i] + array[j] > n:
                    continue
                elif array[i] + array[j] == n:
                    return [array[i], array[j]]
    else:
        for i in range(len(array)):
            parts = entriesThatSum(n - array[i], m - 1, array, exclude + [i])
            if parts is not None:
                return [array[i]] + parts

with open("input/day1.txt") as f:
    lines = [int(line.rstrip()) for line in f]

lines.sort()

entries = entriesThatSum(2020, 2, lines)
print("part1 solution:", reduce(lambda x, y: x * y, entries), entries)

entries = entriesThatSum(2020, 3, lines)
print("part2 solution:", reduce(lambda x, y: x * y, entries), entries)

entries = entriesThatSum(2020, 4, lines)
print("bonus solution:", reduce(lambda x, y: x * y, entries), entries)
