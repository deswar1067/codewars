"""
Complete the function which converts a binary number (given as a string) to a decimal number.

"""

import codewars_test as test


def bin_to_decimal(inp):
    return int(inp, base=2)


bin_to_decimal('1010101')

test.it('bin_to decimal("0") should return 0')
test.assert_equals(bin_to_decimal('0'), 0)

test.it('bin_to decimal("1") should return 1')
test.assert_equals(bin_to_decimal('1'), 1)

test.it('bin_to decimal("10") should return 2')
test.assert_equals(bin_to_decimal('10'), 2)

test.it('bin_to decimal("11") should return 3')
test.assert_equals(bin_to_decimal('11'), 3)

test.it('bin_to decimal("100") should return 4')
test.assert_equals(bin_to_decimal('110'), 4)

test.it('bin_to decimal("101") should return 4')
test.assert_equals(bin_to_decimal('101'), 5)

test.it('bin_to decimal("1001001") should return 73')
test.assert_equals(bin_to_decimal('1001001'), 73)
