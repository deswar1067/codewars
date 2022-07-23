"""
My PC got infected by a strange virus. It only infects my text files and replaces random letters by *, li*e th*s
 (like this).

Fortunately, I discovered that the virus hides my censored letters inside root directory.

It will be very tedious to recover all these files manually, so your goal is to implement uncensor function that does
the hard work automatically.

Examples
uncensor("*h*s *s v*ry *tr*ng*", "Tiiesae") ➜ "This is very strange"

uncensor("A**Z*N*", "MAIG") ➜ "AMAZING"

uncensor("xyz", "") ➜ "xyz"
"""

import codewars_test as test

des = 'Odslpr'
print(des[1:])


def uncensor(infected, discovered):
    for i in infected:
        if i == "*":
            infected = infected.replace(i, discovered[0], 1)
            discovered = discovered[1:]

    return infected


uncensor("*h*s *s v*ry *tr*ng*", "Tiiesae")


@test.describe('Ce*s*r*d Strings')
def examples():
    @test.it("Example Tests")
    def example_fixed():
        data = [
            ('*h*s *s v*ry *tr*ng*', 'Tiiesae', 'This is very strange'),
            ('A**Z*N*', 'MAIG', 'AMAZING'),
            ('xyz', '', 'xyz'),
            ('', '', ''),
            ('***', 'abc', 'abc')
        ]

        for infected, discovered, result in data:
            test.assert_equals(uncensor(infected, discovered), result)

# Best solution:
# def uncensor(infected, discovered):
#     return infected.replace('*', '{}').format(*discovered)
