import pytest


class NegativeNumbersNotAllowed(Exception):
    pass


class StringCalculator:
    def add(self, numbers: str) -> int:
        # if the input string is empty, return 0
        if not numbers:
            return 0

        # Replace all occurrences of '\n' with ','
        numbers = numbers.replace('\n', ',')

        # split the input string into parts using the comma as a delimiter
        parts = numbers.split(",")

        # Check if any negative numbers are present and raise an exception if so
        if '-' in numbers:
            negatives = []
            for part in parts:
                if '-' in part:
                    negatives.append(part)
            raise NegativeNumbersNotAllowed("negatives not allowed: " + ", ".join(map(str, negatives)))

        # initialize a variable to hold the sum
        sum = 0

        # iterate over the parts and add them to the sum
        for part in parts:
            # check if it bigger than 1000
            if int(part) <= 1000:
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
    ("3,4,5,6", 18),  # Test case: numbers = "3,4,5,6", expected result = 18
])
def test_add_an_unknown_amount_of_numbers(numbers, expected):
    calculator = StringCalculator()
    result = calculator.add(numbers)
    assert result == expected


# Test the "add" method to handle new lines between numbers
@pytest.mark.parametrize("numbers, expected", [
    ("2\n3,4,1", 10),  # Test case: numbers = "2\n3,4,1", expected result = 10
    ("2\n3,4\n6", 15),  # Test case: numbers = "2\n3,4\n6", expected result = 15
])
def test_to_handle_new_lines_between_numbers(numbers, expected):
    calculator = StringCalculator()
    result = calculator.add(numbers)
    assert result == expected


# Test the "add" method to ensure that it raises an exception when negative numbers are present
@pytest.mark.parametrize("numbers, expected_message", [
    ("-1,2,-3", "negatives not allowed: -1, -3"),  # Test case: numbers = "-1,2,-3"
    ("1,-4,-10", "negatives not allowed: -4, -10"),  # Test case: numbers = "1,-4,-10"
])
def test_negative_numbers_not_allowed(numbers, expected_message):
    calculator = StringCalculator()

    with pytest.raises(NegativeNumbersNotAllowed) as e:
        calculator.add(numbers)

    assert str(e.value) == expected_message


# Test to add numbers bigger than 1000
@pytest.mark.parametrize("numbers, expected_sum", [
    ("2,1001", 2),  # Test case: numbers = "2,1001", expected_sum = 2
    ("3,2000", 3),  # Test case: numbers = "3,2000", expected_sum = 3
    ("10000,5000,6000,2000", 0),  # Test case: numbers = "10000,5000,6000,2000", expected_sum = 0
])
def test_add_numbers_bigger_than_1000(numbers, expected_sum):
    calculator = StringCalculator()
    assert calculator.add(numbers) == expected_sum
