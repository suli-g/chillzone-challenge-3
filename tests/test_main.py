from main import (
    one,
    two,
    three,
    four,
    five,
    six,
    seven,
    eight,
    nine,
    plus,
    minus,
    divided_by,
    times,
)


def test_callable_ints_are_callable():
    """
    Tests that numbers are callable.

    Fixtures:
    - numbers
    """

    assert one() == 1
    assert four() == 4
    assert seven() == 7


def test_operations_work_on_ints():
    """
    Tests that operations are callable directly on int values.

    Fixtures:
    - operations
    """

    assert plus(1)(2) == 3
    assert minus(2)(1) == -1


def test_operations_work_on_numbers():
    """
    Tests that operations are callable on numbers.

    Fixtures:
    - operations
    - numbers
    """

    assert one(plus(four())) == 5
    assert seven(minus(four())) == 3


def test_division_returns_integer():
    """
    Tests that operations are callable on numbers.

    Fixtures:
    - operations
    - numbers
    """

    assert four(divided_by(seven())) == 0
    assert seven(divided_by(four())) == 1


def test_works_with_challenge_test_cases():
    assert seven(times(five())) == 35
    assert four(plus(nine())) == 13
    assert eight(minus(three())) == 5
    assert six(divided_by(two())) == 3
