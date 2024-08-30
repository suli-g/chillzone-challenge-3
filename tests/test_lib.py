import pytest
from lib import operation, number


@pytest.fixture
def operations() -> list[callable]:
    """
    Defines some test operations to be used in unit tests.

    Operations:
    - plus
    - minus
    - times
    - divided_by
    """

    plus = operation(lambda x, y: x + y)
    minus = operation(lambda x, y: x - y)

    return [
        plus, minus
    ]


@pytest.fixture
def numbers() -> list[int]:
    """
    Defines some numbers to be used in unit tests.

    Numbers:
    1 - The second number.
    4 - The fifth number.
    7 - The eigth number.
    """
    return [
        number(1), number(4), number(7)
    ]


def test_callable_ints_are_callable(numbers):
    """
    Tests that numbers are callable.

    Fixtures:
    - numbers
    """
    one, four, seven = numbers

    assert one() == 1
    assert four() == 4
    assert seven() == 7


def test_operations_work_on_ints(operations):
    """
    Tests that operations are callable directly on int values.

    Fixtures:
    - operations
    """
    plus, minus = operations

    assert plus(1)(2) == 3
    assert minus(2)(1) == -1


def test_operations_work_on_numbers(operations, numbers):
    """
    Tests that operations are callable on numbers.

    Fixtures:
    - operations
    - numbers
    """
    one, four, seven = numbers
    plus, minus = operations

    assert one(plus(four())) == 5
    assert seven(minus(four())) == 3
