import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(num):
            return num>1 and all(num%i!=0 for i in range(2,int(math.sqrt(num)+1)))
        def get_palindrome_even(num): # 1234 -> 12344321
            return int(str(num)+str(num)[::-1])
        def get_palindrome_odd(num): # 1234 -> 1234321
            return int(str(num)+str(num)[:-1][::-1])

        for length in range(1,6):
            for i in range(10**(length-1),10**length):
                res = get_palindrome_odd(i)
                if res>=n and is_prime(res):
                    return res

            for i in range(1,6):
                res = get_palindrome_even(i)
                if res>=n and is_prime(res):
                    return res


class MyTestCase(unittest.TestCase):
    def test1(self):
        n = 6
        Output= 7
        self.assertEqual(Output, get_sol().primePalindrome(n))
    def test2(self):
        n = 8
        Output= 11
        self.assertEqual(Output, get_sol().primePalindrome(n))
    def test3(self):
        n = 13
        Output= 101
        self.assertEqual(Output, get_sol().primePalindrome(n))
    def test4(self):
        n = 2
        Output= 2
        self.assertEqual(Output, get_sol().primePalindrome(n))
    def test5(self):
        n = 1
        Output= 2
        self.assertEqual(Output, get_sol().primePalindrome(n))
    def test6(self):
        n = 1215122
        Output= 1218121
        self.assertEqual(Output, get_sol().primePalindrome(n))
    def test7(self):
        n = 121512
        Output= 1003001
        self.assertEqual(Output, get_sol().primePalindrome(n))
