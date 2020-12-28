"""
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Example:

high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
Notes:

All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
"""


numbers = "4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"


def high_and_low(numbers):
    """
     creates a list of numbers from the string provided
     Returns the max and min
    """
    list_num = [int(i) for i in numbers.split()]
    return f"{max(list_num)} {min(list_num)}"


if __name__ == '__main__':
    print(high_and_low(numbers))
