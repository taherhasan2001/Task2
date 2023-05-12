import pytest


class StringCalculator:
    def add(self, numbers: str) -> int:
        # if the input string is empty, return 0
        if not numbers:
            return 0

        # split the input string into parts using the comma as a delimiter
        parts = numbers.split(",")

        # initialize a variable to hold the sum
        sum = 0

        # iterate over the parts and add them to the sum
        for part in parts:
            sum += int(part)

        # return the sum
        return sum


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


# Test the "add" method with a two number as input
@pytest.mark.parametrize("numbers, expected", [
    ("1,4", 5),  # Test case: numbers = "1,4", expected result = 5
    ("20,2", 22),  # Test case: numbers = "20,2", expected result = 22
])
def test_add_two_numbers(numbers, expected):
    calculator = StringCalculator()
    result = calculator.add(numbers)
    assert result == expected


# Test the "add" method with unknown amount of numbers as input
@pytest.mark.parametrize("numbers, expected", [
    ("2,3,4,1", 10),  # Test case: numbers = "2,3,4,1", expected result = 10
    ("3,4,5,6", 18),  # Test case: numbers = "3,4,5,6", expected result = 14
])
def test_add_an_unknown_amount_of_numbers(numbers, expected):
    calculator = StringCalculator()
    result = calculator.add(numbers)
    assert result == expected
