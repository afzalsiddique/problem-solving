import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        li1 = version1.split('.')
        li2 = version2.split('.')
        n1,n2=len(li1),len(li2)
        li1.extend('0'*(max(n1,n2)-n1))
        li2.extend('0'*(max(n1,n2)-n2))
        li1 = [int(x) for x in li1]
        li2 = [int(x) for x in li2]
        if li1==li2:
            return 0
        elif li1>li2:
            return 1
        return -1


class MyTestCase(unittest.TestCase):
    def test1(self):
        version1,version2 = "1.01",  "1.001"
        Output= 0
        self.assertEqual(Output, get_sol().compareVersion(version1,version2))
    def test2(self):
        version1,version2 = "1.0",  "1.0.0"
        Output= 0
        self.assertEqual(Output, get_sol().compareVersion(version1,version2))
    def test3(self):
        version1,version2 = "0.1",  "1.1"
        Output= -1
        self.assertEqual(Output, get_sol().compareVersion(version1,version2))
    def test4(self):
        version1,version2 = "1.0.1",  "1"
        Output= 1
        self.assertEqual(Output, get_sol().compareVersion(version1,version2))
    def test5(self):
        version1,version2 = "7.5.2.4",  "7.5.3"
        Output= -1
        self.assertEqual(Output, get_sol().compareVersion(version1,version2))
    # def test6(self):
