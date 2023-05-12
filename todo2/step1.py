# Import the necessary pytest module
import pytest

class StringCalculator:
    def add(self, numbers: str) -> int:
        # if the input string is empty, return 0
        if not numbers:
            return 0

        # split the input string into parts using the comma as a delimiter
        parts = numbers.split(",")

        # if there is only one part, return that part as an integer
        if len(parts) == 1:
            return int(parts[0])

        # if there are two parts, add them together and return the sum as an integer
        elif len(parts) == 2:
            return int(parts[0]) + int(parts[1])

        # if there are more than two parts, raise a TypeError
        else:
            raise TypeError("Too many numbers")


# test the "add" method with an empty string as input
def test_add_empty_string():
    calculator = StringCalculator()
    assert calculator.add("") == 0


# Test the "add" method with a single number as input
@pytest.mark.parametrize("numbers, expected", [
    ("5", 5),  # Test case: numbers = "5", expected result = 5
    ("10", 10),  # Test case: numbers = "10", expected result = 10
])
def test_add_single_number(numbers, expected):
    calculator = StringCalculator()
    result = calculator.add(numbers)
    # Check if the result matches the expected value
    assert result == expected


# Define the test function using the pytest.mark.parametrize decorator
@pytest.mark.parametrize("numbers, expected", [
    ("1,4", 5),  # Test case: numbers = "1,4", expected result = 5
    ("20,2", 22),  # Test case: numbers = "20,2", expected result = 22
])
def test_add_two_numbers(numbers, expected):
    calculator = StringCalculator()
    result = calculator.add(numbers)
    assert result == expected
