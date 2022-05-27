"""
Digital Cypher assigns to each letter of the alphabet unique number. For example:

 a  b  c  d  e  f  g  h  i  j  k  l  m
 1  2  3  4  5  6  7  8  9 10 11 12 13
 n  o  p  q  r  s  t  u  v  w  x  y  z
14 15 16 17 18 19 20 21 22 23 24 25 26
Instead of letters in encrypted word we write the corresponding number, eg. The word scout:

 s  c  o  u  t
19  3 15 21 20
Then we add to each obtained digit consecutive digits from the key. For example. In case of key equal to 1939 :

   s  c  o  u  t
  19  3 15 21 20
 + 1  9  3  9  1
 ---------------
  20 12 18 30 21

   m  a  s  t  e  r  p  i  e  c  e
  13  1 19 20  5 18 16  9  5  3  5
+  1  9  3  9  1  9  3  9  1  9  3
  --------------------------------
  14 10 22 29  6 27 19 18  6  12 8
Task
Write a function that accepts str string and key number and returns an array of integers representing encoded str.

Input / Output
The str input string consists of lowercase characters only.
The key input number is a positive integer.


"""

import string
import codewars_test as test
import math


def encode(message, key):
    dict2 = [a for a in list(string.ascii_lowercase)]  #создаем список букв
    dict1 = [a for a in range(1, 27)]                  #список чисел
    dict3 = dict(zip(dict2, dict1))                    #создаем словарь ключ-буква , значение-цифра
    string_1 = [int(i) for i in str(key)]              #создаем список элементов из данных key
    value = [dict3[i] for i in message]                #создаем список элементов значений из словаря по данным messange
    if len(value) > len(string_1):
        string_2 = string_1 * math.ceil(len(value) / len(string_1))
        res = list(sum(i) for i in zip(value, string_2))
        return res
    else:
        res = list(sum(i) for i in zip(value, string_1))
        return res
    # res = [sum(i) for i in itertools.zip_longest(value, string_1, fillvalue=None)]
    # result = [value[i] + string_1[i] for i in range(len(value))]


encode("dwdwd", 134)


test.assert_equals(encode("scout", 1939), [20, 12, 18, 30, 21])
test.assert_equals(encode("masterpiece", 1939), [14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8])


"""
Best solution 

from itertools import cycle

def encode(message, key):
    return [ord(a) - 96 + int(b) for a,b in zip(message,cycle(str(key)))]
"""