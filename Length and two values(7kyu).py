"""
Given an integer n and two other values, build an array of size n filled with these two values alternating.

Examples
5, true, false     -->  [true, false, true, false, true]
10, "blue", "red"  -->  ["blue", "red", "blue", "red", "blue", "red", "blue", "red", "blue", "red"]
0, "one", "two"    -->  []
"""

import itertools
import  codewars_test as test

import math
def alternate(n, first_value, second_value):
    if n/2 != 0:
        c = math.ceil(n/2)
        d = math.floor(n/2)
    else:
        c = int(n/2)
        d = int(n/2)
    l1 = list(itertools.repeat(first_value, c))
    print(l1)
    l2 = list(itertools.repeat(second_value, d))
    print(l2)
    l3 = []
    for i, j in itertools.zip_longest(l1, l2, fillvalue='kl' ):
        l3.append(i)
        l3.append(j)
        if j == 'kl':
            l3.remove(j)
    return l3



@test.describe("Tests")
def test_group():
    @test.it("Sample tests")
    def test_case():
        test.assert_equals(alternate(5, True, False), [True, False, True, False, True])
        test.assert_equals(alternate(20, "blue", "red"), ['blue', 'red', 'blue', 'red', 'blue', 'red', 'blue', 'red', 'blue', 'red', 'blue', 'red', 'blue', 'red', 'blue', 'red', 'blue', 'red', 'blue', 'red'])
        test.assert_equals(alternate(0, "lemons", "apples"), [])