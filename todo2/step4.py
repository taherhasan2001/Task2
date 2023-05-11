class StringCalculator:
    def add(self, numbers: str) -> int:
        # if the input string is empty, return 0
        if not numbers:
            return 0

        # Check if the input string contains a custom delimiter
        if numbers.startswith('//'):
            delimiter, numbers = numbers.split('\n', maxsplit=1)
            delimiter = delimiter[2:]  # Remove the initial '//'
        else:
            delimiter = ","

        # split the input string into parts using the comma as a delimiter
        parts = numbers.split(delimiter)

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

# test the "add" method with a single number as input
def test_add_single_number():
    calculator = StringCalculator()
    assert calculator.add("5") == 5

# test the "add" method with two numbers as input
def test_add_two_numbers():
    calculator = StringCalculator()
    assert calculator.add("2,3") == 5

# test the "add" method with unknown amount of numbers as input
def test_add_an_unknown_amount_of_numbers():
    calculator = StringCalculator()
    assert calculator.add("2,3,4,1") == 10

def test_to_handle_different_delimiters():
    calculator = StringCalculator()
    assert calculator.add("//;\n1;2") == 3