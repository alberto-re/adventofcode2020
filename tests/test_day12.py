from day12 import Ship, manhattan, navigate


PART1_INSTR = """\
F10
N3
F7
R90
F11
"""


def test_ship_starting_coords():
    ship = Ship()
    assert ship.coordinates == (0, 0)
    assert ship.degrees == 90


def test_ship_rotation_right():
    ship = Ship()
    ship.rotate("R", 90)
    assert ship.degrees == 180
    ship.rotate("R", 90)
    assert ship.degrees == 270
    ship.rotate("R", 90)
    assert ship.degrees == 0
    ship.rotate("R", 270)
    assert ship.degrees == 270


def test_ship_rotation_left():
    ship = Ship()
    ship.rotate("L", 90)
    assert ship.degrees == 0
    ship.rotate("L", 90)
    assert ship.degrees == 270
    ship.rotate("L", 90)
    assert ship.degrees == 180
    ship.rotate("L", 90)
    assert ship.degrees == 90
    ship.rotate("L", 180)
    assert ship.degrees == 270


def test_ship_forward():
    ship = Ship()
    ship.forward(10)
    assert ship.coordinates == (10, 0)
    ship.rotate("R", 180)
    assert ship.coordinates == (10, 0)
    ship.forward(10)
    assert ship.coordinates == (0, 0)
    ship.forward(30)
    assert ship.coordinates == (-30, 0)


def test_manhattan():
    assert manhattan((0, 0), (5, 5)) == 10
    assert manhattan((0, 0), (-3, 5)) == 8
    assert manhattan((0, 0), (17, -8)) == 25


def test_navigate():
    ship = Ship()
    for i in PART1_INSTR.split("\n")[:-1]:
        navigate(ship, i)
    assert ship.coordinates == (17, -8)
    assert manhattan((0, 0), ship.coordinates) == 25
