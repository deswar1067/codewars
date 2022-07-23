"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.


"""
import codewars_test as test


def get_count(sentence):
    c = [char for char in sentence if char == "a" or char == 'e' or char == 'i' or char == 'o' or char == 'u']
    return len(c)


print(get_count('dwfeaq'))


@test.describe("Sample tests")
def sample_tests():
    @test.it("Should count all vowels")
    def all_vowels():
        test.assert_equals(get_count("aeiou"), 5, f"Incorrect answer for \"aeiou\"")

    @test.it("Should not count \"y\"")
    def only_y():
        test.assert_equals(get_count("y"), 0, f"Incorrect answer for \"y\"")

    @test.it("Should return 0 when no vowels")
    def no_vowels():
        test.assert_equals(get_count("bcdfghjklmnpqrstvwxz y"), 0, f"Incorrect answer for \"bcdfghjklmnpqrstvwxz y\"")

    @test.it("Should return 0 for empty string")
    def no_vowels():
        test.assert_equals(get_count(""), 0, f"Incorrect answer for empty string")

    @test.it("Should return 5 for \"abracadabra\"")
    def test_abracadabra():
        test.assert_equals(get_count("abracadabra"), 5, f"Incorrect answer for \"abracadabra\"")
