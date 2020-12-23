#!/usr/bin/env python3
# --- Day 4: Passport Processing ---

import re


def extract_passports(lines):
    passports = [{}]

    for line in lines:
        if line:
            for field in line.split():
                key, value = field.split(":")
                passports[-1][key] = value
        else:
            passports.append({})
    return passports


def required_fields(passport, fields={"byr", "pid", "hcl", "hgt", "ecl", "eyr", "iyr"}):
    return fields.issubset(set(passport.keys()))


def valid_fields(passport):
    if not 1920 <= int(passport["byr"]) <= 2002:
        return False
    if not 2010 <= int(passport["iyr"]) <= 2020:
        return False
    if not 2020 <= int(passport["eyr"]) <= 2030:
        return False
    matches = re.match("(\d+)(cm|in)", passport["hgt"])
    if not matches:
        return False
    qty = int(matches.group(1))
    unit = matches.group(2)
    if unit == "cm" and not 150 <= qty <= 193:
        return False
    if unit == "in" and not 59 <= qty <= 76:
        return False
    if not re.match("#[0-9a-f]{6}", passport["hcl"]):
        return False
    if not passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    if len(passport["pid"]) != 9 or not passport["pid"].isdigit():
        return False
    return True


lines = []
with open("input/day4.txt") as f:
    lines = [line.rstrip() for line in f]

passports = extract_passports(lines)

print("part1 solution:", sum(map(required_fields, passports)))

print(
    "part2 solution:",
    sum(map(lambda x: required_fields(x) and valid_fields(x), passports)),
)
