'''
Write a function that counts how many different ways you can make change for an amount of money, given an array of coin denominations. For example, there are 3 ways to give change for 4 if you have coins with denomination 1 and 2:

1+1+1+1, 1+1+2, 2+2.
The order of coins does not matter:

1+1+2 == 2+1+1
Also, assume that you have an infinite amount of coins.

Your function should take an amount to change and an array of unique denominations for the coins:

  count_change(4, [1,2]) # => 3
  count_change(10, [5,2,3]) # => 4
  count_change(11, [5,7]) # => 0
'''


'''
Best solution using recursion
'''
def count_change_two(money, coins):
    # bug in the test: when money = 0 return 1
    if money == 0:
        return 1
    # check if there is some money
    if money < 0:
        return 0
    # check if there is some coins
    if not coins:
        return 0
    # Recursive function:
    return count_change(money-coins[-1],coins) + count_change(money,coins[:-1])


def count_change(money, coins):
    # initialise an empty array (ways[0] = 1 to fix a bug: when money = 0 return 1)
    ways = [1] + [0] * money
    for coin in coins:
        for i in range(coin, money + 1):
            ways[i] += ways[i - coin]
        # print(coin, ways)
    return ways[money]

   
if __name__ == "__main__":
    import codewars_test as test
    test.assert_equals(3, count_change(4, [1,2]))
    test.assert_equals(4, count_change(10, [5,2,3]))
    test.assert_equals(0, count_change(11, [5,7]))
