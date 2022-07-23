"""
Given an integer, if the length of it's digits is a perfect square, return a square block of sqroot(length) * sqroot(length). If not, simply return "Not a perfect square!".

Examples:

1212 returns:

12
12

Note: 4 digits so 2 squared (2x2 perfect square). 2 digits on each line.

123123123 returns:

123
123
123

Note: 9 digits so 3 squared (3x3 perfect square). 3 digits on each line.
"""
import codewars_test as test


def square_it(digits):
    c = len(str(digits)) ** 0.5
    if c.is_integer():
        chunks = [str(digits)[i:i + int(c)] for i in range(0, len(str(digits)), int(c))]
        return "\n".join(chunks)
    else:
        return "Not a perfect square!"


print(square_it(1111))

test.assert_equals(square_it(1), "1")
test.assert_equals(square_it(222), "Not a perfect square!")
test.assert_equals(square_it(234562342342), "Not a perfect square!")
test.assert_equals(square_it(88989), "Not a perfect square!")
test.assert_equals(square_it(112141568), "112\n141\n568")
