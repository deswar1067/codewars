"""
A Narcissistic Number is a number of length l in which the sum of its digits to the power of l is equal to the original number. If this seems confusing, refer to the example below.

Ex: 153, where l = 3 ( the number of digits in 153 )
13 + 53 + 33 = 153

Write a function that, given n, returns whether or not n is a Narcissistic Number.
"""

import codewars_test as test


def is_narcissistic(num):
    c = [int(i) ** len(str(num)) for i in str(num)]
    print(sum(c))
    if sum(c) == num:
        return True
    else:
        return False


print(is_narcissistic(1634))

test.assert_equals(is_narcissistic(153), True)
test.assert_equals(is_narcissistic(201), False)
test.assert_equals(is_narcissistic(259), False)
test.assert_equals(is_narcissistic(371), True)
test.assert_equals(is_narcissistic(407), True)
test.assert_equals(is_narcissistic(595), False)
test.assert_equals(is_narcissistic(825), False)
test.assert_equals(is_narcissistic(1634), True)
