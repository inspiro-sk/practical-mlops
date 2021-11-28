from math_functions import add, divide


def test_add():
    assert 5 == add(2, 3)
    assert 30 == add(21, 9)


def test_divide():
    assert 1.5 == divide(3, 2)
    assert 2.0 == divide(10, 5)
    assert 3.3333 == divide(10, 3)
