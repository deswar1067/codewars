"""TYour job at E-Corp is both boring and difficult. It isn't made any easier by the fact that everyone constantly
wants to have a meeting with you, and that the meeting rooms are always taken!

In this kata, you will be given an array. Each value represents a meeting room. Your job? Find the first empty one
and return its index (N.B. There may be more than one empty room in some test cases).

'X' --> busy
'O' --> empty
If all rooms are busy, return "None available!"

"""

import codewars_test as test


def meeting(rooms):
    try:
        c = rooms.index('O')
        return c
    except ValueError:
        return 'None available!'


print(meeting(["X"]))


@test.describe("meeting")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(meeting(['X', 'O', 'X']), 1)
        test.assert_equals(meeting(['O', 'X', 'X', 'X', 'X']), 0)
        test.assert_equals(meeting(['X', 'X', 'O', 'X', 'X']), 2)
        test.assert_equals(meeting(['X']), 'None available!')
