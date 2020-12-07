#!/usr/bin/env python3
# --- Day 6: Custom Customs ---

lines = []
with open("input/day6.txt") as f:
    lines = [line.rstrip() for line in f]


def groups(lines):
    groups, persons = [], []
    for line in lines:
        if not len(line) and len(persons):
            groups.append(persons)
            persons = []
        else:
            persons.append([c for c in line])
    if len(persons):
        groups.append(persons)
    return groups


def count_anyone_yes(group):
    questions = {}
    for person in group:
        for question in person:
            questions[question] = 1
    return len(questions.keys())


def count_everyone_yes(group):
    questions = {}
    for person in group:
        for question in person:
            if question in questions:
                questions[question] += 1
            else:
                questions[question] = 1
    count = 0
    for key, value in questions.items():
        if value == len(group):
            count += 1

    return count


print("part1 solution:", sum([count_anyone_yes(g) for g in groups(lines)]))

print("part2 solution:", sum([count_everyone_yes(g) for g in groups(lines)]))
