# Import the pytest library
import pytest


# Define a function that returns the sum of two numbers
def add(x, y):
    return x + y


# Define a test class that inherits from pytest.TestCase
class TestAdd:
    # Write a test method that starts with test_
    def test_add_positive(self):
        # Use the assert keyword to check if the expected and actual outcomes match
        assert add(2, 3) == 5

    # Write another test method that starts with test_
    def test_add_negative(self):
        # Use the assert keyword to check if the expected and actual outcomes match
        assert add(-2, -3) == -5


@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
    ],
)
def test_addition(input_a, input_b, expected):
    assert add(input_a, input_b) == expected
