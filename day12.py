#!/usr/bin/env python3
# --- Day 12: Rain Risk ---

from typing import Tuple


class Ship:
    def __init__(self) -> None:
        self._coordinates = (0, 0)
        self._orientation = 90

    def move(self, direction: str, units: int) -> None:
        assert direction in ["N", "W", "S", "E"]
        if direction == "N":
            self._coordinates = (self._coordinates[0], self._coordinates[1] + units)
        elif direction == "S":
            self._coordinates = (self._coordinates[0], self._coordinates[1] - units)
        elif direction == "W":
            self._coordinates = (self._coordinates[0] - units, self._coordinates[1])
        elif direction == "E":
            self._coordinates = (self._coordinates[0] + units, self._coordinates[1])

    def forward(self, units: int) -> None:
        self.move(self.cardinal, units)

    def rotate(self, direction: str, degrees: int) -> None:
        assert degrees % 90 == 0
        assert direction in ["L", "R"]
        if direction == "R":
            self._orientation += degrees
        elif direction == "L":
            self._orientation -= degrees
        self._orientation %= 360

    @property
    def coordinates(self) -> Tuple[int, int]:
        return self._coordinates

    @property
    def degrees(self) -> int:
        return self._orientation

    @property
    def cardinal(self) -> int:
        if self._orientation == 0:
            return "N"
        elif self._orientation == 90:
            return "E"
        elif self._orientation == 180:
            return "S"
        elif self._orientation == 270:
            return "W"


def navigate(ship: Ship, instruction: str) -> None:
    (action, value) = (instruction[0], int(instruction[1:]))
    if action in ["N", "S", "W", "E"]:
        ship.move(action, value)
    if action in ["L", "R"]:
        ship.rotate(action, value)
    if action in ["F"]:
        ship.forward(value)


def manhattan(start: Tuple[int, int], end: Tuple[int, int]) -> int:
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


if __name__ == "__main__":
    data = None
    with open("input/day12.txt") as f:
        data = f.read()

    ship = Ship()
    for i in data.split("\n")[:-1]:
        navigate(ship, i)

    print("part1 solution:", manhattan((0, 0), ship.coordinates))
