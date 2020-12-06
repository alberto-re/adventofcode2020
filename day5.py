#!/usr/bin/env python3
# --- Day 5: Binary Boarding ---

lines = []
with open("input/day5.txt") as f:
    lines = [line.rstrip() for line in f]


def decode_binary(bseat):
    chars = [c for c in bseat]
    lower, upper, left, right = 0, 127, 0, 7
    for row in range(7):
        if chars[row] == "F":
            upper -= ((upper - lower) // 2) + 1
        else:
            lower += ((upper - lower) // 2) + 1
    for col in range(3):
        if chars[col + 7] == "L":
            right -= ((right - left) // 2) + 1
        else:
            left += ((right - left) // 2) + 1
    assert lower == upper
    assert left == right
    return lower, left


def sit_id(coord):
    (row, col) = coord
    return row * 8 + col


def find_missing_seat(seats_map):
    for row_offset in range(63):
        for col in range(0, 8):
            if seats_map[64 + row_offset][col] == 0:
                return (64 + row_offset, col)
            elif seats_map[64 - row_offset][col] == 0:
                return (64 - row_offset, col)


seats = list(map(decode_binary, lines))

seats_ids = map(sit_id, seats)

print("part1 solution:", max(seats_ids))

seats_map = [[0 for j in range(8)] for i in range(128)]

for seat in seats:
    (row, col) = seat
    seats_map[row][col] = 1


print("part2 solution:", sit_id(find_missing_seat(seats_map)))
