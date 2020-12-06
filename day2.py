#!/usr/bin/env python3
# --- Day 2: Password Philosophy ---


def extract_policy(line):
    policy, pwd = line.split(": ")
    minmax, char = policy.split()
    cmin, cmax = map(int, minmax.split("-"))
    return {"pwd": pwd, "char": char, "cmin": cmin, "cmax": cmax}


def rule1(pwd, char, cmin, cmax):
    count = 0
    for c in pwd:
        if c == char:
            count += 1
    return cmin <= count <= cmax


def rule2(pwd, char, cmin, cmax):
    return (pwd[cmin - 1] == char) != (pwd[cmax - 1] == char)


def password_valid(policies, rule):
    valid = 0
    for policy in policies:
        if rule(**policy):
            valid += 1
    return valid


with open("input/day2.txt") as f:
    policies = [extract_policy(line.rstrip()) for line in f]

print("part1 solution:", password_valid(policies, rule1))
print("part2 solution:", password_valid(policies, rule2))
