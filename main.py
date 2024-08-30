"""
My implementation for ChillZone Challenge #3.

Functions:
    Numbers:
        - zero
        - one
        - two
        - three
        - four
        - five
        - six
        - seven
        - eight
        - nine

    Operations:
        - plus : Performs addition of the given numbers.
        - minus : Performs subtraction of the given numbers.
        - times : Performs multiplication of the given numbers.
        - divided_by : Performs integer division of the given numbers.
"""
from src.lib import number, operation

# Define the numbers for the challenge.
zero, one, two, three, four, five, six, seven, eight, nine = map(
    number, range(10)
)

# Define the functions for the challenge:
plus, minus, times, divided_by = map(operation, [
    lambda x, y: x + y,
    lambda x, y: x - y,
    lambda x, y: x * y,
    lambda x, y: x // y
])


def main():
    """
    The main implementation for this challenge.
    """
    print(zero())
    print(one(minus(two())))


if __name__ == "__main__":
    main()
