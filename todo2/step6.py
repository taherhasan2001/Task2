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
            negatives=[]
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

# test the "add" method with a single number as input
def test_add_single_number():
    calculator = StringCalculator()
    assert calculator.add("5") == 5

# test the "add" method with two numbers as input
def test_add_two_numbers():
    calculator = StringCalculator()
    assert calculator.add("2,3") == 5

# test the "add" method with an unknown amount of numbers as input
def test_add_an_unknown_amount_of_numbers():
    calculator = StringCalculator()
    assert calculator.add("2,3,4,1") == 10

# test the "add" method with new lines between numbers as input
def test_to_handle_new_lines_between_numbers():
    calculator = StringCalculator()
    assert calculator.add("2\n3,4,1") == 10

# test the "add" method to ensure that it raises an exception when negative numbers are present
def test_negative_numbers_not_allowed():
    calculator = StringCalculator()

    with pytest.raises(NegativeNumbersNotAllowed) as e:
        calculator.add("-1,2,-3")

    assert str(e.value) == "negatives not allowed: -1, -3"

# test to add numbers bigger than 1000
def test_add_numbers_bigger_than_1000():
    calculator = StringCalculator()
    assert calculator.add("2,1001") == 2
