'''
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngr
'''

''' first draft '''
def solution(string,markers):
    # separate each lines
    res = string.split('\n')
    
    for i in range(len(res)):
        # remove the comments
        for mak in markers:
            res[i] = str(res[i]).split(mak)[0]
        # remove a trailing white space
        res[i] = res[i].strip()
    
    # put the lines back together
    res = '\n'.join(res)
    return res
    

''' refactored '''
def solution(string, markers):
    lines = string.split('\n') # separate each lines
    for marker in markers:
        # remove the comments and the trailing space
        lines = [line.split(marker)[0].rstrip() for line in lines]
    return '\n'.join(lines) # put the lines back together

if __name__ == "__main__":
    import codewars_test as Test
    # -*- coding: utf-8 -*-
    Test.assert_equals(solution("apples, pears # and bananas\ngrapes\nbananas #apples", ["#", "!"]), "apples, pears\ngrapes\nbananas")
    Test.assert_equals(solution("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")
    Test.assert_equals(solution("apples, pears # and bananas\ngrapes\nbananas !apples", []), "apples, pears # and bananas\ngrapes\nbananas !apples")