import re
class StringCalculator:
    def add(self, numbers: str) -> int:
        # if the input string is empty, return 0
        if not numbers:
            return 0
        delimiters = []
        second_part = ''

        if numbers[0:2] == '//' and '\n' in numbers and numbers[2] == '[':  # check if its in the format of step 7 ex : //[***]\n1***2***3
            first_part = numbers[2:].split('\n')[0]  # [***]
            second_part = numbers[len(first_part) + 3:]  # the numbers part ex : 1,2***3,4
            if first_part[len(first_part) - 1] == ']' and first_part.count('[') == 1:
                first_part = first_part.replace('[', '')
                first_part = first_part.replace(']', '')
            delimiters.append(first_part)




        # Check if the input string contains a custom delimiter format in step 4  ==> //;\n1;2
        if numbers.startswith('//') and not delimiters:  # if delimiters are Empty list
            delimiter, numbers = numbers.split('\n', maxsplit=1)
            delimiter = delimiter[2:]  # Remove the initial '//'
        else:
            delimiter = ","

        # split the input string into parts using the comma as a delimiter
        if not delimiters:
            parts = numbers.split(delimiter)
        else:
            for i in range(len(delimiters)):
                second_part = second_part.replace(delimiters[i], ',')
            parts = second_part.split(',')



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
    assert calculator.add("//+\n1+2") == 3

def test_to_handle_Delimiters_can_be_of_any_length():
    calculator = StringCalculator()
    assert calculator.add("//[***]\n1,2,3***4") == 10

