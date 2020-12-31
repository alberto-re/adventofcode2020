from day11 import Grid, look_direction, step, step_until_equilibrium

PART1_INIT = """\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""


PART1_ROUND1 = """\
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
"""

PART1_ROUND2 = """\
#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##
"""


PART1_ROUND3 = """\
#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##
"""


PART1_ROUND4 = """\
#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##
"""

PART1_ROUND5 = """\
#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##
"""

PART2_INIT = """\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""

PART2_ROUND1 = """\
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
"""

PART2_ROUND2 = """\
#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#
"""

PART2_ROUND3 = """\
#.L#.##.L#
#L#####.LL
L.#.#..#..
##L#.##.##
#.##.#L.##
#.#####.#L
..#.#.....
LLL####LL#
#.L#####.L
#.L####.L#
"""

PART2_ROUND4 = """\
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##LL.LL.L#
L.LL.LL.L#
#.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLL#.L
#.L#LL#.L#
"""

PART2_ROUND5 = """\
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.#L.L#
#.L####.LL
..#.#.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#
"""

PART2_ROUND6 = """\
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#
"""

PART2_SIGHT_DATA1 = """\
.......#.
...#.....
.#.......
.........
..#L....#
....#....
.........
#........
...#.....
"""

PART2_SIGHT_DATA2 = """\
.............
.L.L.#.#.#.#.
.............
"""


def test_grid_from_text_dimensions():
    grid = Grid.from_text(PART1_INIT)
    assert (grid.cols, grid.rows) == (10, 10)


def test_grid_from_text_content():
    grid = Grid.from_text(PART1_INIT)
    assert grid[0, 0] == "L"
    assert grid[2, 1] == "."
    assert grid[2, 8] == "."
    assert grid[4, 0] == "L"
    assert grid[4, 1] == "."
    assert grid[9, 9] == "L"


def test_look_direction_only_adjacent():
    grid = Grid.from_text(PART1_INIT)
    assert look_direction((1, 1), (-1, -1), grid, 1) == "L"
    assert look_direction((1, 1), (-1, 0), grid, 1) == "."
    assert look_direction((3, 3), (0, 1), grid, 1) == "."
    grid = Grid.from_text(PART1_ROUND2)
    assert look_direction((0, 0), (0, 1), grid, 1) == "."
    assert look_direction((0, 0), (-1, 1), grid, 1) == "."
    assert look_direction((0, 0), (1, 0), grid, 1) == "#"
    assert look_direction((0, 0), (1, 1), grid, 1) == "L"


def test_look_direction():
    grid = Grid.from_text(PART2_SIGHT_DATA1)
    assert look_direction((4, 3), (0, 1), grid, -1) == "#"
    assert look_direction((4, 3), (1, 1), grid, -1) == "#"
    assert look_direction((4, 3), (1, 0), grid, -1) == "#"
    assert look_direction((4, 3), (1, -1), grid, -1) == "#"
    assert look_direction((4, 3), (-1, 0), grid, -1) == "#"
    assert look_direction((4, 3), (-1, -1), grid, -1) == "#"
    assert look_direction((4, 3), (0, -1), grid, -1) == "#"
    grid = Grid.from_text(PART2_SIGHT_DATA2)
    assert look_direction((1, 1), (0, 1), grid, -1) == "L"


def test_steps_part1():
    assert Grid.from_text(PART1_ROUND1) == step(Grid.from_text(PART1_INIT), 1, 4)
    assert Grid.from_text(PART1_ROUND2) == step(Grid.from_text(PART1_ROUND1), 1, 4)
    assert Grid.from_text(PART1_ROUND3) == step(Grid.from_text(PART1_ROUND2), 1, 4)
    assert Grid.from_text(PART1_ROUND4) == step(Grid.from_text(PART1_ROUND3), 1, 4)
    assert Grid.from_text(PART1_ROUND5) == step(Grid.from_text(PART1_ROUND4), 1, 4)


def test_step_until_equilibrium_part1():
    grid = Grid.from_text(PART1_INIT)
    grid = step_until_equilibrium(grid)
    assert grid.occupied == 37


def test_steps_part2():
    assert Grid.from_text(PART2_ROUND1) == step(Grid.from_text(PART2_INIT), -1, 5)
    assert Grid.from_text(PART2_ROUND2) == step(Grid.from_text(PART2_ROUND1), -1, 5)
    assert Grid.from_text(PART2_ROUND3) == step(Grid.from_text(PART2_ROUND2), -1, 5)
    assert Grid.from_text(PART2_ROUND4) == step(Grid.from_text(PART2_ROUND3), -1, 5)
    assert Grid.from_text(PART2_ROUND5) == step(Grid.from_text(PART2_ROUND4), -1, 5)
    assert Grid.from_text(PART2_ROUND6) == step(Grid.from_text(PART2_ROUND5), -1, 5)


def test_step_until_equilibrium_part2():
    grid = Grid.from_text(PART2_INIT)
    grid = step_until_equilibrium(grid, -1, 5)
    assert grid.occupied == 26

