"""
I have a cat and a dog.

I got them at the same time as kitten/puppy. That was humanYears years ago.

Return their respective ages now as [humanYears,catYears,dogYears]

NOTES:

humanYears >= 1
humanYears are whole numbers only
Cat Years
15 cat years for first year
+9 cat years for second year
+4 cat years for each year after that
Dog Years
15 dog years for first year
+9 dog years for second year
+5 dog years for each year after that

"""

import codewars_test as test


def human_years_cat_years_dog_years(human_years):
    cat_year = float
    dog_year = float
    if human_years == 1:
        cat_year = 15
        dog_year = 15
        return [human_years, cat_year, dog_year]

    elif 1 <= human_years <= 2:
        cat_year = 15 + (human_years - 1) * 9
        dog_year = 15 + (human_years - 1) * 9
        return [human_years, cat_year, dog_year]

    elif human_years > 2:
        cat_year = 24 + (human_years - 2) * 4
        dog_year = 24 + (human_years - 2) * 5
        return [human_years, cat_year, dog_year]


human_years_cat_years_dog_years(14)


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("one")
    def _():
        test.assert_equals(human_years_cat_years_dog_years(1), [1, 15, 15])

    @test.it("two")
    def _():
        test.assert_equals(human_years_cat_years_dog_years(2), [2, 24, 24])

    @test.it("ten")
    def _():
        test.assert_equals(human_years_cat_years_dog_years(10), [10, 56, 64])
