import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def h(a,b):
            i=0
            j=n-1
            while i<j and a[i]==b[j]:
                i+=1
                j-=1
            if i>=j: return True
            while i<j and a[i]==a[j]:
                i+=1
                j-=1
            if i>=j: return True
            while i<j and b[i]==b[j]:
                i+=1
                j-=1
            if i>=j: return True
            return False

        n=len(a)
        return h(a,b) or h(b,a)

class MyTestCase(unittest.TestCase):
    def test_1(self):
        a,b = "x", "y"
        Output= True
        self.assertEqual(Output, get_sol().checkPalindromeFormation(a,b))
    def test_2(self):
        a,b = "abdef",  "fecab"
        Output= True
        self.assertEqual(Output, get_sol().checkPalindromeFormation(a,b))
    def test_3(self):
        a,b = "ulacfd", "jizalu"
        Output= True
        self.assertEqual(Output, get_sol().checkPalindromeFormation(a,b))
    def test_4(self):
        a,b = "xbdef",  "xecab"
        Output= False
        self.assertEqual(Output, get_sol().checkPalindromeFormation(a,b))
    def test_5(self):
        a,b = "pvhmupgqeltozftlmfjjde", "yjgpzbezspnnpszebzmhvp"
        Output= True
        self.assertEqual(Output, get_sol().checkPalindromeFormation(a,b))
