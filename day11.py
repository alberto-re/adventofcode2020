#!/usr/bin/env python3
# --- Day 11: Seating System ---


from typing import List, Tuple, Callable

# fmt: off
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1),
              ( 0, -1),          ( 0, 1),
              ( 1, -1), ( 1, 0), ( 1, 1)]
# fmt: on


class Grid:
    def __init__(self, grid: List[List[str]]) -> None:
        self._grid = grid
        self._rows = len(grid)
        self._cols = len(grid[0])

    @property
    def cols(self) -> int:
        return self._cols

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def occupied(self) -> int:
        return sum([sum([1 for cell in row if cell == "#"]) for row in self._grid])

    @staticmethod
    def from_text(text: str) -> "Grid":
        return Grid([[cell for cell in row] for row in text.split("\n")[:-1]])

    def __getitem__(self, pos: Tuple[int, int]) -> str:
        m, n = pos
        return self._grid[m][n]

    def __str__(self) -> str:
        return "\n".join(["".join(row) for row in self._grid])

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Grid):
            return self._grid == other._grid
        return False


def look_direction(position: Tuple[int, int], direction: Tuple[int, int], grid: Grid, limit: int) -> str:
    (m, n) = position
    (md, nd) = direction
    radius = 0
    while limit == -1 or radius < limit:
        radius += 1
        if 0 <= m + md * radius < grid.rows and 0 <= n + nd * radius < grid.cols:
            if grid[m + md * radius, n + nd * radius] != ".":
                return grid[m + md * radius, n + nd * radius]
        else:
            return "."
    return grid[m + md * radius, n + nd * radius]


def evaluate_position(position: Tuple[int, int], grid: Grid, limit: int, tolerance: int) -> str:
    occupied = 0
    for direction in DIRECTIONS:
        if look_direction(position, direction, grid, limit) == "#":
            occupied += 1
    if occupied == 0 and grid[position] == "L":
        return "#"
    if occupied >= tolerance and grid[position] == "#":
        return "L"
    return grid[position]


def step(grid: Grid, limit: int, tolerance: int) -> Grid:
    new_grid = []
    for m in range(grid.rows):
        new_row = []
        for n in range(grid.cols):
            new_row.append(evaluate_position((m, n), grid, limit, tolerance))
        new_grid.append(new_row)
    return Grid(new_grid)


def step_until_equilibrium(grid: Grid, limit: int = 1, tolerance: int = 4) -> Grid:
    prev = None
    while grid != prev:
        prev = grid
        grid = step(grid, limit, tolerance)
    return grid


if __name__ == "__main__":
    data = None
    with open("input/day11.txt") as f:
        data = f.read()

    grid = Grid.from_text(data)
    grid = step_until_equilibrium(grid)
    print("part1 solution:", grid.occupied)

    grid = Grid.from_text(data)
    grid = step_until_equilibrium(grid, -1, 5)
    print("part2 solution:", grid.occupied)
