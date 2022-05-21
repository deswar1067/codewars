"""
Given an input of an array of digits, return the array with each digit incremented by its position in the array: the first digit will be incremented by 1, the second digit by 2, etc. Make sure to start counting your positions from 1 ( and not 0 ).

Your result can only contain single digit numbers, so if adding a digit with its position gives you a multiple-digit number, only the last digit of the number should be returned.

Notes:
return an empty array if your array is empty
arrays will only contain numbers so don't worry about checking that
Examples:
[1, 2, 3]  -->  [2, 4, 6]   #  [1+1, 2+2, 3+3]

[4, 6, 9, 1, 3]  -->  [5, 8, 2, 5, 8]  #  [4+1, 6+2, 9+3, 1+4, 3+5]
                                       #  9+3 = 12  -->  2
"""
import codewars_test as test


def incrementer(nums):
    return [i + j if (i + j) < 10 else (i + j) % 10 for i, j in zip(nums, range(1, 90))]
    # return [ (v+i)%10 for i,v in enumerate(nums,1) ]
    # return [(i + j) % 10 for i, j in zip(nums, range(1, 90))]

print(incrementer([1, 4, 5, 8]))


@test.describe("Sample tests")
def tests():
    @test.it("Some examples")
    def tests():
        test.assert_equals(incrementer([]), [])
        test.assert_equals(incrementer([1, 2, 3]), [2, 4, 6])
        test.assert_equals(incrementer([4, 6, 7, 1, 3]), [5, 8, 0, 5, 8])
        test.assert_equals(incrementer([3, 6, 9, 8, 9]), [4, 8, 2, 2, 4])
        test.assert_equals(incrementer([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 8]),
                           [2, 4, 6, 8, 0, 2, 4, 6, 8, 9, 0, 1, 2, 2])
