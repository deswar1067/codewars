"""So you've found a meeting room - phew! You arrive there ready to present, and find that someone has taken one or
more of the chairs!! You need to find some quick.... check all the other meeting rooms to see if all of the chairs
are in use.

Your meeting room can take up to 8 chairs. need will tell you how many have been taken. You need to find that many.

Find the spare chairs from the array of meeting rooms. Each meeting room tuple will have the number of occupants as a
string. Each occupant is represented by 'X'. The room tuple will also have an integer telling you how many chairs
there are in the room.

You should return an array of integers that shows how many chairs you take from each room in order, up until you have
the required amount.

example:

[['XXX', 3], ['XXXXX', 6], ['XXXXXX', 9], ['XXX',2]] when you need 4 chairs:

result -> [0, 1, 3] no chairs free in room 0, take 1 from room 1, take 3 from room 2. no need to consider room 3 as
you have your 4 chairs already.

If you need no chairs, return "Game On". If there aren't enough spare chairs available, return "Not enough!".

"""

import codewars_test as test


def meeting(rooms, need):
    c = []
    for i in rooms:
        b = (i[1] - len(i[0]))
        if b < 0 and sum(c) < need:
            c.append(0)
        elif sum(c) < need:
            c.append(b)
        else:
            continue

    if need == 0:
        return "Game On"
    elif sum(c) < need:
        return 'Not enough!'
    elif sum(c) > need:
        c[-1] = need - (sum(c) - c[-1])
    return c


print((meeting([["XXX", 1], ["XXXXXX", 6], ["X", 2], ["XXXXXX", 8], ["X", 3], ["XXX", 1]], 5)))

test.describe("Basic tests")
test.assert_equals(meeting([["XXX", 1], ["XXXXXX", 6], ["X", 2], ["XXXXXX", 8], ["X", 3], ["XXX", 1]], 5),
                   [0, 0, 1, 2, 2])
test.assert_equals(meeting([["XXX", 3], ["XXXXX", 6], ["XXXXXX", 9]], 4), [0, 1, 3])

test.assert_equals(meeting([["XX", 2], ["XXXX", 6], ["XXXXX", 4]], 0), "Game On")
test.assert_equals(meeting([["XX", 2], ["XXXX", 6], ["XXXXX", 4]], 8), "Not enough!")
test.assert_equals(meeting([["XX", 2], ["XXXX", 6], ["XXXXX", 4]], 2), [0, 2])



# Best solution:


# def meeting(rooms, need):
#     if need == 0: return "Game On"
#
#     result = []
#     for people, chairs in rooms:
#         taken = min(max(chairs - len(people), 0), need)
#         result.append(taken)
#         need -= taken
#         if need == 0: return result
#
#     return "Not enough!"


