import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def minFlips(self, s: str) -> int:
        n=len(s)
        even_zero, odd_zero, even_one, odd_one = 0,0,0,0
        for i in range(n):
            if s[i]=='0':
                odd_zero += i%2
                even_zero += i%2==0
            else:
                odd_one += i%2
                even_one += i%2==0

        option1 = even_zero+odd_one
        option2 = odd_zero+even_one
        option3 = float('inf')
        option4 = float('inf')
        li = deque(s)

        if n%2:
            for i in range(n):
                even_one,odd_one = odd_one,even_one
                even_zero,odd_zero = odd_zero,even_zero
                if li[0]=='0':
                    even_zero+=1
                    odd_zero-=1
                else:
                    even_one+=1
                    odd_one-=1
                option3 = min(option3,even_zero+odd_one)
                option4 = min(option4,odd_zero+even_one)
                li.append(li.popleft())
        return min(option1,option2,option3, option4)

class MyTestCase(unittest.TestCase):
    def test1(self):
        s = "111000"
        Output= 2
        self.assertEqual(Output, get_sol().minFlips(s))
    def test2(self):
        s = "010"
        Output= 0
        self.assertEqual(Output, get_sol().minFlips(s))
    def test3(self):
        s = "1110"
        Output= 1
        self.assertEqual(Output, get_sol().minFlips(s))
    def test4(self):
        s = "01001001101"
        Output= 2
        self.assertEqual(Output, get_sol().minFlips(s))
    def test5(self):
        s = "1101010"
        Output= 0
        self.assertEqual(Output, get_sol().minFlips(s))
    # def test6(self):
    # def test7(self):
