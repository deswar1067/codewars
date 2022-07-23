"""
In this kata you get the start number and the end number of a region and should return the count of all numbers except
 numbers with a 5 in it. The start and the end number are both inclusive!
"""
import codewars_test as test


def dont_give_me_five(start, end):
    list2 = [i for i in range(start, end + 1)]
    res = []
    for a in list2:
        if '5' not in str(a):
            res.append(a)
    print(res)
    return len(res)


print(dont_give_me_five(55, 122))

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(dont_give_me_five(1,9), 8)
        test.assert_equals(dont_give_me_five(4,17), 12)
        test.assert_equals(dont_give_me_five(55,122), 59)
