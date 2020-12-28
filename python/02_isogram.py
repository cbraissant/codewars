"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case
"""

string = 'Dermatoglyphics'
string = 'aba is not a safe word'


# My solution
def is_isogram(string):
    '''
    Go through each characters of the string.
    Check if the character if found anywhere else in the string.
    '''
    for i in range(0, len(string)):
        if string[i].lower() in string[i + 1:].lower():
            return False
    return True


# Best solution
def is_isogram(string):
    '''
    Converts all the letters to lower case and put them in a set.
    The set will remove the duplicates.
    Check that the length of the string is the same as the length of the set.
    '''
    return len(string) == len(set(string.lower()))


if __name__ == '__main__':
    print(is_isogram(string))
