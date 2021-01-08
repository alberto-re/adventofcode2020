#!/usr/bin/env python3
# --- Day 13: Shuttle Search ---

from typing import List


def earliest_bus(timestamp: int, buses: List[int]):
    delta = timestamp
    best = None
    for bus in buses:
        if timestamp % bus == 0:
            return (bus, 0)
        else:
            _delta = (((timestamp // bus) + 1) * bus) - timestamp
            if _delta < delta:
                delta = _delta
                best = bus
    return (best, delta)


if __name__ == "__main__":
    with open("input/day13.txt") as f:
        timestamp = int(f.readline())
        buses = [int(x) for x in f.readline().split(",") if x != "x"]

    bus, delta = earliest_bus(timestamp, buses)
    print("part1 solution:", bus * delta)
