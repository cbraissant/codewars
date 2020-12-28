'''
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]
'''


def array_diff(a, b):
    '''
    create a new list of number
    iterate through the first list
    append the number if not in the second list

    list = []
    for c in a:
        if c not in b:
            list.append(c)
    '''
    return [c for c in a if c not in b]


if __name__ == '__main__':
    print(array_diff(a, b))
