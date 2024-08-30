from typing import Callable, Optional, Union

type Number = Callable[[int], Union[int, Number]]
type Operation = Callable[[int, int], int]
type RightOperation = Callable[[int], int]
type LeftOperation = Callable[[int], RightOperation]


def number(value: int) -> Number:
    """ Creates a number that can be used in operations.

    Args:
        value: The value of the number.

    Returns:
        callable: _description_
    """
    def apply(operation: Optional[callable] = None) -> Union[int, callable]:
        return operation(value) if operation else value
    return apply


def operation(callback: Operation) -> LeftOperation:
    """ Creates an operation that can be performed on numbers.

    Args:
        callback: The operation to be performed.

    Returns:
        int: The result of the operation.
    """
    def apply(right_operand: int) -> RightOperation:
        return lambda left_operand: callback(left_operand, right_operand)

    return apply
