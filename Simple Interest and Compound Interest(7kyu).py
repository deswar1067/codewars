"""
Simple interest on a loan is calculated by simply taking the initial amount (the principal, p) and multiplying it by a rate of interest (r) and the number of time periods (n).

Compound interest is calculated by adding the interest after each time period to the amount owed, then calculating the next interest payment based on the principal PLUS the interest from all previous periods.

Given a principal p, interest rate r, and a number of periods n, return an array [ total owed under simple interest, total owed under compound interest ]

Notes:

Round all answers to the nearest integer
Principal will always be an integer between 0 and 9999
interest rate will be a decimal between 0 and 1
number of time periods will be an integer between 0 and 50
"""

import codewars_test as test


def interest(p, r, n):
    a = 1
    sum_inv = p
    while a <= n:
        sum_inv = sum_inv + sum_inv * r
        a += 1
    return [round(p * r * n + p), round(sum_inv)]


print(interest(628, 0.82, 2))


# def interest(M, P, Y):
#     return [round(M + M*P*Y), round(M*(1+P)**Y)]


@test.describe("Sample tests")
def tests():
    @test.it("Some examples")
    def tests():
        test.assert_equals(interest(100, 0.1, 1), [110, 110])
        test.assert_equals(interest(100, 0.1, 2), [120, 121])
        test.assert_equals(interest(100, 0.1, 10), [200, 259])
