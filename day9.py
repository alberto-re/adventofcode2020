#!/usr/bin/env python3
# --- Day 9: Encoding Error ---


numbers = []
with open("input/day9.txt") as f:
    numbers = [int(line.rstrip()) for line in f]


def first_not_sum(numbers, n_before):
    for i in range(len(numbers)):
        if i < n_before - 1:
            continue
        sums = []
        for j in range(i - n_before, i):
            for k in range(i - n_before, i):
                if numbers[j] != numbers[k]:
                    sums.append(numbers[j] + numbers[k])
        if numbers[i] not in sums:
            return i


def continuous_that_sums_to(numbers, n):
    for i in range(len(numbers)):
        crange = []
        for j in range(i, len(numbers)):
            crange.append(numbers[j])
            crange_total = sum(crange)
            if crange_total > n:
                break
            if crange_total == n:
                return min(crange) + max(crange)


invalid = first_not_sum(numbers, 25)
print("part1 solution:", numbers[invalid])

print("part2 solution:", continuous_that_sums_to(numbers, numbers[invalid]))
