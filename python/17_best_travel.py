'''
John and Mary want to travel between a few towns A, B, C ... Mary has on a sheet of paper a list of distances between these towns. ls = [50, 55, 57, 58, 60]. John is tired of driving and he says to Mary that he doesn't want to drive more than t = 174 miles and he will visit only 3 towns.

Which distances, hence which towns, they will choose so that the sum of the distances is the biggest possible to please Mary and John?

Example:
With list ls and 3 towns to visit they can make a choice between: [50,55,57],[50,55,58],[50,55,60],[50,57,58],[50,57,60],[50,58,60],[55,57,58],[55,57,60],[55,58,60],[57,58,60].

The sums of distances are then: 162, 163, 165, 165, 167, 168, 170, 172, 173, 175.

The biggest possible sum taking a limit of 174 into account is then 173 and the distances of the 3 corresponding towns is [55, 58, 60].

The function chooseBestSum (or choose_best_sum or ... depending on the language) will take as parameters t (maximum sum of distances, integer >= 0), k (number of towns to visit, k >= 1) and ls (list of distances, all distances are positive or null integers and this list has at least one element). The function returns the "best" sum ie the biggest possible sum of k distances less than or equal to the given limit t, if that sum exists, or otherwise nil, null, None, Nothing, depending on the language.

With C++, C, Rust, Swift, Go, Kotlin, Dart return -1.

Examples:
ts = [50, 55, 56, 57, 58] choose_best_sum(163, 3, ts) -> 163

xs = [50] choose_best_sum(163, 3, xs) -> nil (or null or ... or -1 (C++, C, Rust, Swift, Go)

ys = [91, 74, 73, 85, 73, 81, 87] choose_best_sum(230, 3, ys) -> 228

Note:
don't modify the input list ls
'''


'''
number of different trip possible:
(order doesn't matter, no duplicates)
          len(ls)!
n = -------------------
    k! ( len(ls) - k )!

exemple:
ls = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
len(ls) = 17
k = 4
        17!         17!
n = ---------- = -------- = 2380
    4! (17-4)!   4! * 13!
'''

'''
normal version
'''
def choose_best_sum(t, k, ls):
    from itertools import combinations
    # get all the differents combinations of number possible
    combos = list(combinations(ls, k))
    # calculate the sum of the distances
    distances = []
    for combo in combos:
        dist = sum(list(combo))
        # only if the distance is not greater than the max
        if dist <= t:
            distances.append(dist)
    # check if a suitable distance exist
    if distances:
        # get the maximum distance possible
        return max(distances)
    else:
        return None
'''
condensed version
'''
def choose_best_sum(t, k, ls):
    from itertools import combinations
    return max([sum(i) for i in combinations(ls, k) if sum(i) <= t], default=None)    
        
    

if __name__ == "__main__":
    import codewars_test as Test
    # Test.it("Bigger numbers")
    xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
    # ls = [1, 2, 3, 4, 5, 6]
    # print(choose_best_sum(192, 4, xs))
    Test.assert_equals(choose_best_sum(230, 4, xs), 230)
    Test.assert_equals(choose_best_sum(430, 5, xs), 430)
    Test.assert_equals(choose_best_sum(430, 8, xs), None)
