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


# test the "add" method with a single number as input
def test_add_single_number():
    calculator = StringCalculator()
    assert calculator.add("5") == 5


# test the "add" method with two numbers as input
def test_add_two_numbers():
    calculator = StringCalculator()
    assert calculator.add("2,3") == 5
