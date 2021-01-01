'''
Write a function called sumIntervals/sum_intervals() that accepts an array of intervals, and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.

Intervals
Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always be less than the second value. Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.

Overlapping Intervals
List containing overlapping intervals:

[
   [1,4],
   [7, 10],
   [3, 5]
]
The sum of the lengths of these intervals is 7. Since [1, 4] and [3, 5] overlap, we can treat the interval as [1, 5], which has a length of 4.

Examples:
sumIntervals( [
   [1,2],
   [6, 10],
   [11, 15]
] ); // => 9

sumIntervals( [
   [1,4],
   [7, 10],
   [3, 5]
] ); // => 7

sumIntervals( [
   [1,5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
] ); // => 19
'''


'''
my solution
Fairly verbose and create a new list of value.
Can do better and do the sum in the main loop
'''
def sum_of_intervals(intervals):
    # sort the tuple by starting number
    st = sorted(intervals, key=lambda tup: tup[0])
    lst = []
    lst.append(list(st[0]))
    for i in st[1:]:
        # first number of tuple already in the list
        if i[0] <= lst[-1][1]:
            # update new list with the bigger number
            lst[-1][1] = max(lst[-1][1], i[1])
        else:
            lst.append(list(i))
    sum = 0
    for j in lst:
        sum += j[1] - j[0]
    return sum


'''
BEST PRACTICE
Sort the list of tuple and loop through all of them
Check if the first number is bigger than the maxa
    - update the max
Check if the second number is bigger than the max (therefore bigger than the first)
    - update the max and the sum
'''
def sum_of_intervals(intervals):
    total = 0
    # initialise the max number to -inf to handle negative numbers
    max_n = float("-inf")
    # enumerate through all the sorted values
    for a, b in sorted(intervals):
        # update the max number if bigger than the first
        if a > max_n:
            max_n = a
        # update the sum and the max number if bigger than the second as well
        if b > max_n:
            total = total + (b-max_n)
            max_n = b
    return total


'''
MOST CLEVER
Add all the numbers of each tuple in a set of value.
The set of value will remove duplicates (therefore taking care of overlapping)
The length of the set is equivalent to the sum of all intervals
'''
def sum_of_intervals(intervals):
    result = set()
    # enumerate through all the tuples
    for start, stop in intervals:
        # enumerate through the values of the tuple
        for x in range(start, stop):
            # add each number to a set
            resultat.add(x)
    return len(result)
            
        


        
if __name__ == "__main__":
    import codewars_test as Test
    Test.assert_equals(sum_of_intervals([(1, 5)]), 4)
    Test.assert_equals(sum_of_intervals([(1, 5), (6, 10)]), 8)
    Test.assert_equals(sum_of_intervals([(1, 5), (1, 5)]), 4)
    Test.assert_equals(sum_of_intervals([(-19, 40), (7, 10), (3, 5)]), 59)
