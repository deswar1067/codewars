"""
The BOPE is the squad of special forces of police that usually handles the operations in the Favelas in Rio de Janeiro.

In this Kata you have to write a function that determine the number of magazines that every soldier has to have in
his bag.

You will receive the weapon and the number of streets that they have to cross. Considering that every street the
officer shoots 3 times. Bellow there is the relation of weapons:

PT92 - 17 bullets
M4A1 - 30 bullets
M16A2 - 30 bullets
PSG1 - 5 bullets

Example:

["PT92", 6] => 2 (6 streets 3 bullets each)
["M4A1", 6] => 1

The return Will always be an integer so as the params.
"""

import math
import codewars_test as test
from typing import Tuple


def mag_number(info: Tuple[str, int]) -> int:
    data = {'PT92': 17, 'M4A1': 30, 'M16A2': 30, 'PSG1': 5}
    c = info[1] * 3 / data[info[0]]
    return math.ceil(c)


print(mag_number(("PT92", 12)))


@test.describe("Sample Tests")
def test_group():
    test_cases = (
        # input, expected -- feel free to add more cases if needed
        (("PT92", 6), 2),
        (("M4A1", 8), 1),
        (("M16A2", 19), 2),
        (("PSG1", 31), 19),
        (("PT92", 19), 4),
    )

    @test.it("Should return the number of magazines a soldier needs (Sample tests).")
    def test_case():
        for input, expected in test_cases:
            test.assert_equals(mag_number(input), expected, f"Failed case mag_number({input})")
