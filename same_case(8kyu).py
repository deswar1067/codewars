"""
Write a function that will check if two given characters are the same case.

If either of the characters is not a letter, return -1
If both characters are the same case, return 1
If both characters are letters, but not the same case, return 0
Examples
'a' and 'g' returns 1

'A' and 'C' returns 1

'b' and 'G' returns 0

'B' and 'g' returns 0

'0' and '?' returns -1
"""


def same_case(a, b):
    if a.islower() and b.islower():
        return 1
    elif a.isupper() and b.isupper():
        return 1
    elif a.isupper() and b.islower():
        return 0
    elif a.islower() and b.isupper():
        return 0
    elif ord(a) or ord(b):
        """!, @, #, %, ^ and other"""
    return -1


same_case('A', 'c')
