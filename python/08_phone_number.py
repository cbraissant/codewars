'''
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example:
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
                    ) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!
'''


def create_phone_number(n):
    '''
    - convert each number to a str, and join all of them
    - format the response
    '''
    m = ''.join(map(str, n))
    return f'({m[0:3]}) {m[3:6]}-{m[6:]}'


def create_phone_number(n):
    '''
    simplier one deconstructing the list passed
    '''
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


if __name__ == "__main__":
    print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
