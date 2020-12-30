'''Problem Context
The Fibonacci sequence is traditionally used to explain tree recursion.

def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
This algorithm serves well its educative purpose but it's tremendously inefficient, not only because of recursion, but because we invoke the fibonacci function twice, and the right branch of recursion (i.e. fibonacci(n-2)) recalculates all the Fibonacci numbers already calculated by the left branch (i.e. fibonacci(n-1)).

This algorithm is so inefficient that the time to calculate any Fibonacci number over 50 is simply too much. You may go for a cup of coffee or go take a nap while you wait for the answer. But if you try it here in Code Wars you will most likely get a code timeout before any answers.

For this particular Kata we want to implement the memoization solution. This will be cool because it will let us keep using the tree recursion algorithm while still keeping it sufficiently optimized to get an answer very rapidly.

The trick of the memoized version is that we will keep a cache data structure (most likely an associative array) where we will store the Fibonacci numbers as we calculate them. When a Fibonacci number is calculated, we first look it up in the cache, if it's not there, we calculate it and put it in the cache, otherwise we returned the cached number.

Refactor the function into a recursive Fibonacci function that using a memoized data structure avoids the deficiencies of tree recursion Can you make it so the memoization cache is private to this function?

'''


'''
original solution
(recursion, no cache)
'''
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


'''
my solution
(recursion, with local cache)
'''
cache = {}
def fibonacci(n):
    # print(cache)
    if n in cache:
        return cache[n]
    if n <= 0:
        value = 0
    elif n == 1:
        value = 1
    else:
        value = fibonacci(n-1) + fibonacci(n-2)
    cache[n] = value
    return value


'''
best solution
(using decorator for caching)
'''
def cached(f):
    # define a empty cache for that function
    cache = {}
    def wrapper(k):
        # check if the value is stored in cache
        value = cache.get(k)
        if value is None:
            # call the function and save the value in cache
            value = cache[k] = f(k)
        return value
    return wrapper

@cached
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
    import codewars_test as test
    test.assert_equals(fibonacci(0), 0)
    test.assert_equals(fibonacci(1), 1)
    test.assert_equals(fibonacci(10), 55)
    test.assert_equals(fibonacci(50), 12586269025)
    test.assert_equals(fibonacci(60), 1548008755920)
    test.assert_equals(fibonacci(70), 190392490709135)