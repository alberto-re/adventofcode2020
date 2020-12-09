#!/usr/bin/env python3
# --- Day 7: Handy Haversacks ---

import re


class Bag:
    def __init__(self, color):
        self.color = color
        self.contain = {}
        self.contained = []

    def __str__(self):
        contain = ["%s (%d)" % (c, q) for c, q in self.contain.items()]
        return "Bag<color=%s, contain=%s, contained=%s>" % (
            self.color,
            contain,
            self.contained,
        )


def parse(input_lines):
    struct = dict()
    for line in lines:
        match = re.match("(.+) bags contain (.+).$", line)
        assert match
        color = match.group(1)
        contains = dict()
        for i in match.group(2).split(","):
            if "no other bags" in i:
                continue
            submatch = re.match("\s?(\d+) (.+) bag", i)
            assert submatch
            contains[submatch.group(2)] = int(submatch.group(1))
        struct[color] = contains
    return struct


def contain_eventually(color):
    partial = []
    if len(bags[color].contained) == 0:
        return []
    partial.extend(bags[color].contained)
    for c in bags[color].contained:
        partial.extend(contain_eventually(c))
    return partial


def bags_inside(color):
    partial = 0
    if len(bags[color].contain) == 0:
        return partial
    for c, q in bags[color].contain.items():
        partial += q
        partial += q * bags_inside(c)
    return partial


lines = []
with open("input/day7.txt") as f:
    lines = [line.rstrip() for line in f]

input_struct = parse(lines)

bags = {}
for k in input_struct.keys():
    bags[k] = Bag(k)

for k, v in input_struct.items():
    for c, q in v.items():
        bags[k].contain[c] = q
        bags[c].contained.append(k)


print("part1 solution:", len(set(contain_eventually("shiny gold"))))

print("part2 solution:", bags_inside("shiny gold"))
