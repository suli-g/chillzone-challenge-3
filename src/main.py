from typing import Callable, Optional, Union

type Number = Callable[[int], Union[int, Number]]
type Operation = Callable[[int, int], int]
type RightOperation = Callable[[int], int]
type LeftOperation = Callable[[int], RightOperation]


def integer(value: int) -> Number:
    """Creates a callable integer that can be used in operations.

    Args:
        value: The value of the integer.

    Returns:
        callable: A function that returns this integer's value, or
        performs the specified operation on this integer.
    """

    def apply(operation: Optional[callable] = None) -> Union[int, callable]:
        return int(operation(value) if operation else value)

    return apply


def operation(callback: Operation) -> LeftOperation:
    """Creates an operation that can be performed on numbers.

    Args:
        callback: The operation to be performed.

    Returns:
        int: The result of the operation.
    """

    def apply(right_operand: int) -> RightOperation:
        return lambda left_operand: callback(left_operand, right_operand)

    return apply


# Define the numbers for the challenge.
zero, one, two, three, four, five, six, seven, eight, nine = map(
    integer, range(10)
)

# Define the functions for the challenge:
plus, minus, times, divided_by = map(
    operation,
    [
        lambda x, y: x + y,
        lambda x, y: x - y,
        lambda x, y: x * y,
        lambda x, y: x // y,
    ],
)


def main():
    """
    The main implementation for this challenge.
    """

    print(one(plus(two(minus(three(times(five(divided_by(seven())))))))))


if __name__ == "__main__":
    main()
