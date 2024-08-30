# ChillZone Challenge 3

This time we want to write calculations using functions and get the results. Let's have a look at some examples:

```js
seven(times(five())); // must return 35
four(plus(nine())); // must return 13
eight(minus(three())); // must return 5
six(dividedBy(two())); // must return 3
```

Requirements:

* There must be a function for each number from 0 ("zero") to 9 ("nine")
* There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy
* Each calculation consist of exactly one operation and two numbers

* The most outer function represents the left operand, the most inner function represents the right operand.

Division should be integer division.
For example, this should return `2`, not `2.666666...`:

```js
eight(dividedBy(three()));
```

## Running the Project

```
python 
```

## Types

The following types have been defined:

```python
type Number = Callable[[int], Union[int, Number]]
type Operation = Callable[[int, int], int]
type RightOperation = Callable[[int], int]
type LeftOperation = Callable[[int], RightOperation]
```

## Functions

To make the solution a bit more scalable, the following functions have been defined as well:

```python
def number(value: int) -> Number:
    """
    Creates a number that can be used in operations.

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
```

## Usage

To define a number, the `number()` function may be used:

### Example

```python
one = number(1)
two = number(2)

print(one())  # Output: 1
print(two())  # Output: 2

print(one(plus(two())))  # Output 3
```

## Unit Tests

Unit tests have been implemented using the [PyTest](https://docs.pytest.org/en/stable/) library.

### Development

This project has been implemented using [Poetry](https://python-poetry.org/) and unit tests have been implemented using [PyTest](https://docs.pytest.org/en/stable/). To run unit tests, refer to the relevant documentation for those tools.

#### Setup

1. Clone this repo:

    ```sh
    git clone https://github.com/suli-g/chillzone-challenge-3
    cd chillzone-challenge-3
    ```

2. Install poetry if not yet installed.

    ```sh
    pip install poetry
    ```

3. Check code style and format (using [Ruff](https://docs.astral.sh/ruff/tutorial/)).

    ```sh
    ruff check --fix
    ```

4. Run Unit tests using PyTest:

    ```sh
    pytest
    ```
