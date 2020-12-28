"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

Examples
to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"
"""

text = "this_is_a_test"


def to_camel_case(text):
    '''
    replace the "-" with "_" to manage only one delimiter
    split the words
    Convert to upper case the first letter of all the words but the first one
    '''
    words = text.replace('-', '_').split('_')
    string = words[0]
    for word in words[1:]:
        string = string + word[0].upper() + word[1:].lower()
    return string


def to_camel_case(text):
    '''
    - use the title() function to convert the sentence
    (returns a string where the first character in every word is upper case, 
    If the word contains a number or a symbol, the first letter after that will be converted to upper case)
    - remove the special characters
    - keep the first letter of the sentence
    - return the string if empty
    '''
    return text[0] + text.title().replace('_', '').replace('-', '')[1:] if text else text


def to_camel_case(text):
    '''
   same using a regex instead of double replace
    '''
    import re
    return text[0] + re.sub('[-_]', '', text.title())[1:] if text else text


def to_camel_case(text):
    '''
   same using translate()
    '''
    return text[0] + text.title().translate(str.maketrans('', '-', '_'))[1:] if text else text


if __name__ == '__main__':
    print(to_camel_case('the_stealth_warrior'))
