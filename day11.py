#!/usr/bin/env python3
# --- Day 11: Seating System ---


class Model:
    def __init__(self, data):
        self._states = [self._to_matrix(data)]
        self._dim = [len(self._states[-1]), len(self._states[-1][0])]

    def step(self):
        new_state = []
        for r in range(self._dim[0]):
            new_state.append([])
            for c in range(self._dim[1]):
                value = self._states[-1][r][c]
                occupied = 0
                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        if r == i and c == j:
                            continue
                        if i < 0 or i > self._dim[0] - 1:
                            continue
                        if j < 0 or j > self._dim[1] - 1:
                            continue
                        if self._states[-1][i][j] == "#":
                            occupied += 1
                if value == "L" and occupied == 0:
                    value = "#"
                elif value == "#" and occupied >= 4:
                    value = "L"
                new_state[r].append(value)
        self._states.append(new_state)

    @staticmethod
    def _to_matrix(data):
        m = []
        for line in data.split("\n")[:-1]:
            m.append([x for x in line])
        return m

    @property
    def epochs(self):
        return len(self._states)

    @property
    def stabilized(self):
        return self.epochs > 1 and str(self._states[-1]) == str(self._states[-2])

    @property
    def occupied(self):
        n = 0
        for r in self._states[-1]:
            for c in r:
                if c == "#":
                    n += 1
        return n

    def __str__(self):
        return "\n".join(["".join(r) for r in self._states[-1]]) + "\n"


TEST_INIT = """L.LL.LL.LL
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

TEST_ROUND1 = """#.##.##.##
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

TEST_ROUND2 = """#.LL.L#.##
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

TEST_ROUND3 = """#.##.L#.##
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

TEST_ROUND4 = """#.#L.L#.##
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

TEST_ROUND5 = """#.#L.L#.##
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

model = Model(TEST_INIT)
assert str(model) == TEST_INIT
model.step()
assert str(model) == TEST_ROUND1
model.step()
assert str(model) == TEST_ROUND2
model.step()
assert str(model) == TEST_ROUND3
model.step()
assert str(model) == TEST_ROUND4
model.step()
assert str(model) == TEST_ROUND5


model = Model(TEST_INIT)
while not model.stabilized:
    model.step()

assert model.occupied == 37

model = Model(data)
while not model.stabilized:
    model.step()

data = None
with open("input/day11.txt") as f:
    data = f.read()

print("part1 solution:", model.occupied)
