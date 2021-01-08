#!/usr/bin/env python3
# --- Day 12: Rain Risk ---

from typing import Tuple
from dataclasses import dataclass
from math import cos, sin, radians


@dataclass
class Position:
    x: int = 0
    y: int = 0

    def move(self, direction: str, units: int) -> None:
        if direction == "N":
            self.y += units
        elif direction == "S":
            self.y -= units
        elif direction == "E":
            self.x += units
        elif direction == "W":
            self.x -= units
        else:
            raise ValueError(f"invalid direction {direction}")

    def move_towards(self, waypoint: "Position", units: int) -> None:
        self.x += units * waypoint.x
        self.y += units * waypoint.y

    def rotate(self, direction: str, degrees: int) -> None:
        assert degrees % 90 == 0
        theta = radians(90)
        for _ in range(degrees // 90):
            (x, y) = self.x, self.y
            if direction == "R":
                self.x = x * cos(-theta) - y * sin(-theta)
                self.y = x * sin(-theta) + y * cos(-theta)
            elif direction == "L":
                self.x = x * cos(theta) - y * sin(theta)
                self.y = x * sin(theta) + y * cos(theta)
            else:
                raise ValueError(f"invalid direction {direction}")

    def manhattan(self) -> int:
        return round(abs(self.x) + abs(self.y))


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

    print("part1 solution:", ship.position.manhattan())

    starting_position = Position(0, 0)
    waypoint = Position(10, 1)
    ship = Ship(starting_position)
    for i in data.split("\n")[:-1]:
        navigate(ship, i, waypoint)

    print("part2 solution:", ship.position.manhattan())
