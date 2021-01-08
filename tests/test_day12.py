from day12 import Position, Ship, navigate


PART1_INSTR = """\
F10
N3
F7
R90
F11
"""


def test_position_move():
    pos = Position(0, 0)
    assert pos == Position(0, 0)
    pos.move("N", 30)
    assert pos == Position(0, 30)
    pos.move("E", 40)
    assert pos == Position(40, 30)
    pos.move("S", 20)
    assert pos == Position(40, 10)
    pos.move("W", 75)
    assert pos == Position(-35, 10)


def test_position_move_towards():
    pos = Position(0, 0)
    assert pos == Position(0, 0)
    pos.move_towards(Position(10, 5), 30)
    assert pos == Position(300, 150)
    pos.move_towards(Position(-10, -5), 30)
    assert pos == Position(0, 0)


def test_position_rotate_right():
    pos = Position(7, 7)
    pos.rotate("R", 90)
    assert pos == Position(7, -7)
    pos.rotate("R", 90)
    assert pos == Position(-7, -7)
    pos.rotate("R", 90)
    assert pos == Position(-7, 7)
    pos.rotate("R", 90)
    assert pos == Position(7, 7)


def test_position_rotate_left():
    pos = Position(7, 7)
    pos.rotate("L", 90)
    assert pos == Position(-7, 7)
    pos.rotate("L", 90)
    assert pos == Position(-7, -7)
    pos.rotate("L", 90)
    assert pos == Position(7, -7)
    pos.rotate("L", 90)
    assert pos == Position(7, 7)


def test_position_manhattan():
    assert Position(10, -5).manhattan() == 15
    assert Position(12, 53).manhattan() == 65
    assert Position(-7, -4).manhattan() == 11


def test_ship_starting_coords():
    ship = Ship(Position(0, 0))
    assert ship.position == Position(0, 0)
    assert ship.degrees == 0


def test_ship_rotation_right():
    ship = Ship(Position(0, 0))
    ship.rotate("R", 90)
    assert ship.degrees == 270
    ship.rotate("R", 90)
    assert ship.degrees == 180
    ship.rotate("R", 90)
    assert ship.degrees == 90
    ship.rotate("R", 270)
    assert ship.degrees == 180


def test_ship_rotation_left():
    ship = Ship(Position(0, 0))
    ship.rotate("L", 90)
    assert ship.degrees == 90
    ship.rotate("L", 90)
    assert ship.degrees == 180
    ship.rotate("L", 90)
    assert ship.degrees == 270
    ship.rotate("L", 90)
    assert ship.degrees == 0
    ship.rotate("L", 180)
    assert ship.degrees == 180


def test_ship_forward():
    ship = Ship(Position(0, 0))
    ship.forward(10)
    assert ship.position == Position(10, 0)
    ship.rotate("R", 180)
    assert ship.position == Position(10, 0)
    ship.forward(10)
    assert ship.position == Position(0, 0)
    ship.forward(30)
    assert ship.position == Position(-30, 0)


def test_navigate_part1():
    starting_position = Position(0, 0)
    ship = Ship(starting_position)
    for i in PART1_INSTR.split("\n")[:-1]:
        navigate(ship, i)
    assert ship.position == Position(17, -8)
    assert ship.position.manhattan() == 25

def test_navigate_part2():
    starting_position = Position(0, 0)
    waypoint = Position(10, 1)
    ship = Ship(starting_position)
    for i in PART1_INSTR.split("\n")[:-1]:
        navigate(ship, i, waypoint)
    assert ship.position == Position(214, -72)
    assert ship.position.manhattan() == 286
