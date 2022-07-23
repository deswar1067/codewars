"""
Make multiple functions that will return the sum, difference, modulus, product, quotient, and the exponent respectively.

Please use the following function names:

addition = add

multiply = multiply

division = divide (both integer and float divisions are accepted)

modulus = mod

exponential = exponent

subtraction = subt

"""
import math
import codewars_test as test


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def mod(a, b):
    return a % b


def exponent(a, b):
    return a**b


def subt(a, b):
    return a - b


if __name__ == '__main__':
    add(5, 2)
    multiply(4, 1)
    divide(2, 2)
    mod(15, 5)
    exponent(2, 7)
    subt(12, 4)

test.describe("Multiple Tests")

test.it("addition(2, 3) should return 5")
test.assert_equals(add(2, 3), 5)

test.it("multiply(3, 5) should return 15")
test.assert_equals(multiply(3, 5), 15)

test.it("devision(12, 4) should return 3")
test.assert_equals(divide(12, 4), 3)

test.it("modulus(100, 5) should return 0")    #показывает остаток от деления
test.assert_equals(mod(100, 5), 0)

test.it("exponential(10, 2) should return 100")
test.assert_equals(exponent(10, 2), 100)

test.it("subtraction(5, 1) should return 4")
test.assert_equals(subt(5, 1), 4)

