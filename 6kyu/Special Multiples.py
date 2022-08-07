"""
Some numbers have the property to be divisible by 2 and 3. Other smaller subset of numbers has the property to be
divisible by 2, 3 and 5. Another subset with less abundant numbers may be divisible by 2, 3, 5 and 7. These numbers
have something in common: their prime factors are contiguous primes.

Implement a function that finds the amount of numbers that have the first N primes as factors below a given limit.

Let's see some cases:

count_specMult(3, 200)  =>  6

The first 3 primes are: 2, 3 and 5.

And the found numbers below 200 are: 30, 60, 90, 120, 150, 180.
"""

import math
import sympy
import codewars_test as test


def count_specmult(n, max_val):
    a = list(sympy.primerange(0, 1000))
    # a = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    b = a[0:n]
    c = math.prod(b)  # перемножает числа в списке
    print(c)
    number = [i for i in range(c, max_val + 1, c) if all(i % j == 0 for j in b)]
    return len(number)


print(count_specmult(3, 100))

test.describe("Tests")
test.assert_equals(count_specmult(3, 200), 6)
test.assert_equals(count_specmult(3, 1000), 33)
test.assert_equals(count_specmult(4, 500), 2)
test.assert_equals(count_specmult(4, 1000), 4)
