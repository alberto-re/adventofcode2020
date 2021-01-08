from day13 import earliest_bus


def test_earliest_bus():
    assert earliest_bus(939, [7, 13, 59, 31, 19]) == (59, 5)
