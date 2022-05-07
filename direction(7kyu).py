"""
You have an 8-wind compass, like this:

You receive the direction you are facing (one of the 8 directions: N, NE, E, SE, S, SW, W, NW) and a certain degree to turn (a multiple of 45, between -1080 and 1080); positive means clockwise, and negative means counter-clockwise.

Return the direction you will face after the turn.

"""

import codewars_test as test
import math


def direction(facing, turn):
    compas = {"S": 0, "SW": 45, "W": 90, "NW": 135, "N": 180, "NE": 225, "E": 270, "SE": 315}
    print(compas[facing])
    ret = abs(turn) - math.floor(abs(turn) / 360) * 360
    print(ret)
    if turn < 0:
        side = compas[facing] - ret
        if side < 0:
            side += 360
            for a, i in compas.items():
                if i == side:
                    return a
        else:
            for a, i in compas.items():
                if i == side:
                    return a

    elif turn >= 0:
        side = compas[facing] + ret
        if side >= 360:
            side -= 360
            for a, i in compas.items():
                if i == side:
                    return a
        else:
            for a, i in compas.items():
                if i == side:
                    return a


print(direction("S", 45))


@test.describe("Sample tests")
def tests():
    @test.it("Some examples")
    def tests():
        test.assert_equals(direction("S", 180), "N")
        test.assert_equals(direction("SE", -45), "E")
        test.assert_equals(direction("W", 495), "NE")


"""TWO Version"""
DIRECTIONS = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']


def direction(facing, turn):
    return DIRECTIONS[(turn // 45 + DIRECTIONS.index(facing)) % 8]


print(direction('N', 135))
