#!/usr/bin/env python3
# --- Day 10: Adapter Array ---

from collections import defaultdict


adapters = []
with open("input/day10.txt") as f:
    adapters = [int(line.rstrip()) for line in f]


def find_chain(adapters):
    adapters_sorted = sorted(adapters)
    adapters_sorted.append(adapters_sorted[-1] + 3)
    adapters_sorted.insert(0, 0)
    chain = [0]
    differences = []
    for i in range(1, len(adapters_sorted)):
        diff = adapters_sorted[i] - adapters_sorted[i - 1]
        assert 1 <= diff <= 3
        differences.append(diff)
        chain.append(adapters_sorted[i])
    return chain, differences


def count_jolts(diffs, n_jolts):
    total = 0
    for diff in diffs:
        if diff == n_jolts:
            total += 1
    return total


def count_possible_chains(adapters):
    adapters_sorted = sorted(adapters)
    adapters_sorted.append(adapters_sorted[-1] + 3)
    adapters_sorted.insert(0, 0)
    counts = defaultdict(int, {0: 1})
    for a in adapters_sorted[1:]:
        counts[a] = counts[a - 3] + counts[a - 2] + counts[a - 1]
    return counts[adapters_sorted[-1]]


chain, diffs = find_chain(adapters)

print("part1 solution:", count_jolts(diffs, 1) * count_jolts(diffs, 3))

print("part2 solution:", count_possible_chains(adapters))
