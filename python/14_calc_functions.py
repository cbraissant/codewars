'''
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))
'''
from operator import mul, add, sub, floordiv


def zero(*args): return args[0][1](0, args[0][0]) if args else 0


def one(*args):  # your code here
    return args[0][1](1, args[0][0]) if args else 1


def two(*args):  # your code here
    return args[0][1](2, args[0][0]) if args else 2


def three(*args):  # your code here
    return args[0][1](3, args[0][0]) if args else 3


def four(*args):  # your code here
    return args[0][1](4, args[0][0]) if args else 4


def five(*args):  # your code here
    return args[0][1](5, args[0][0]) if args else 5


def six(*args):  # your code here
    return args[0][1](6, args[0][0]) if args else 6


def seven(*args):  # your code here
    return args[0][1](7, args[0][0]) if args else 7


def eight(*args):  # your code here
    return args[0][1](8, args[0][0]) if args else 8


def nine(*args):  # your code here
    return args[0][1](9, args[0][0]) if args else 9


def plus(*args):  # your code here
    return args[0], add


def minus(*args):  # your code here
    return args[0], sub


def times(*args):  # your code here
    return args[0], mul


def divided_by(*args):  # your code here
    return args[0], floordiv


'''
best solution using lambda functions
'''


def zero(f=None): return 0 if not f else f(0)
def one(f=None): return 1 if not f else f(1)
def two(f=None): return 2 if not f else f(2)
def three(f=None): return 3 if not f else f(3)
def four(f=None): return 4 if not f else f(4)
def five(f=None): return 5 if not f else f(5)
def six(f=None): return 6 if not f else f(6)
def seven(f=None): return 7 if not f else f(7)
def eight(f=None): return 8 if not f else f(8)
def nine(f=None): return 9 if not f else f(9)
def plus(y): return lambda x: x + y
def minus(y): return lambda x: x - y
def times(y): return lambda x: x * y
def divided_by(y): return lambda x: x // y


if __name__ == "__main__":
    print(nine(times(nine())))
    print(str(eight(minus(three()))) + ' expected 5')
