"""
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer
"""


def square_digits(num):
    """
    Iterates through each digit
    Adds the square of each digit to the sum
    """
    digits = str(num)
    squares = ''
    for digit in digits:
        squares += str(int(digit)**2)
    return int(squares)


def square_digits(num):
    """
    Join the square to a string for each digit
    """
    return int(''.join(str(int(n)**2) for n in str(num)))


if __name__ == '__main__':
    print(square_digits(9119))
