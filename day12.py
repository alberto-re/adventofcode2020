#!/usr/bin/env python3
# --- Day 12: Rain Risk ---

from typing import Tuple
from math import cos, sin, radians


DIRECTIONS = ["N", "W", "S", "E"]


class Position:

    """A class representing a pair of x, y coordinates"""

    def __init__(self, x: int = 0, y: int = 0) -> None:
        self._x = x
        self._y = y

    def move(self, direction: str, units: int) -> None:
        assert direction in DIRECTIONS
        if direction == "N":
            self._y += units
        elif direction == "S":
            self._y -= units
        elif direction == "E":
            self._x += units
        elif direction == "W":
            self._x -= units

    def move_towards(self, waypoint: "Position", units: int) -> None:
        relx, rely = units * waypoint.x, units * waypoint.y
        self._x += relx
        self._y += rely

    def rotate(self, direction: str, degrees: int) -> None:
        assert degrees % 90 == 0
        assert direction in ["L", "R"]
        theta = radians(90)
        for _ in range(degrees // 90):
            (x, y) = self._x, self._y
            if direction == "R":
                self._x = x * cos(-theta) - y * sin(-theta)
                self._y = x * sin(-theta) + y * cos(-theta)
            if direction == "L":
                self._x = x * cos(theta) - y * sin(theta)
                self._y = x * sin(theta) + y * cos(theta)

    def manhattan(self, other: "Position") -> int:
        return round(abs(self.x - other.x) + abs(self.y - other.y))

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Position):
            return self.x == other.x and self.y == other.y
        if isinstance(other, tuple):
            return self.x == other[0] and self.y == other[1]
        return False


class Ship:
    def __init__(self, position: Position) -> None:
        self._position = Position(position.x, position.y)
        self._orientation = 0

    def move(self, direction: str, units: int) -> None:
        self._position.move(direction, units)

    def move_towards(self, waypoint: "Position", units: int) -> None:
        self._position.move_towards(waypoint, units)

    def forward(self, units: int) -> None:
        self.move(self.cardinal, units)

    def rotate(self, direction: str, degrees: int) -> None:
        assert degrees % 90 == 0
        assert direction in ["L", "R"]
        if direction == "R":
            self._orientation -= degrees
        else:
            self._orientation += degrees
        self._orientation %= 360

    @property
    def position(self) -> Position:
        return self._position

    @property
    def degrees(self) -> int:
        return self._orientation

    @property
    def cardinal(self) -> int:
        if self._orientation == 0:
            return "E"
        elif self._orientation == 90:
            return "N"
        elif self._orientation == 180:
            return "W"
        elif self._orientation == 270:
            return "S"


def navigate(ship: Ship, instruction: str, waypoint: Position = None) -> None:
    (action, value) = (instruction[0], int(instruction[1:]))
    if action in ["N", "S", "W", "E"]:
        if waypoint:
            waypoint.move(action, value)
        else:
            ship.move(action, value)
    if action in ["L", "R"]:
        if waypoint:
            waypoint.rotate(action, value)
        else:
            ship.rotate(action, value)
    if action in ["F"]:
        if waypoint:
            ship.move_towards(waypoint, value)
        else:
            ship.forward(value)


if __name__ == "__main__":
    data = None
    with open("input/day12.txt") as f:
        data = f.read()

    starting_position = Position(0, 0)
    ship = Ship(starting_position)
    for i in data.split("\n")[:-1]:
        navigate(ship, i)

    print("part1 solution:", ship.position.manhattan(starting_position))

    starting_position = Position(0, 0)
    waypoint = Position(10, 1)
    ship = Ship(starting_position)
    for i in data.split("\n")[:-1]:
        navigate(ship, i, waypoint)

    print("part2 solution:", ship.position.manhattan(starting_position))
