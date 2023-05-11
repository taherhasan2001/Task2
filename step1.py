class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        parts = numbers.split(",")
        if len(parts) == 1:
            return int(parts[0])
        elif len(parts) == 2:
            return int(parts[0]) + int(parts[1])
        else:
            raise TypeError("Too many numbers")


def test_add_empty_string():
    calculator = StringCalculator()
    assert calculator.add("") == 0

def test_add_single_number():
    calculator = StringCalculator()
    assert calculator.add("5") == 5

def test_add_two_numbers():
    calculator = StringCalculator()
    assert calculator.add("2,3") == 5
