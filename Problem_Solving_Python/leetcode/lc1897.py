import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n=len(words)
        di=defaultdict(int)
        for word in words:
            for letter in word:
                di[letter]+=1
        for letter in di:
            if di[letter]%n!=0: return False
        return True

class tester(unittest.TestCase):
    def test01(self):
        ranges = [[1,2],[3,4],[5,6]]
        left = 2
        right = 5
        Output= True
        self.assertEqual(Output,get_sol().isCovered(ranges, left, right))
    def test02(self):
        ranges = [[1,10],[10,20]]
        left = 21
        right = 21
        Output= False
        self.assertEqual(Output,get_sol().isCovered(ranges, left, right))
    def test03(self):
        n = 3
        Output= 35
        self.assertEqual(Output,get_sol().countVowelStrings(n))
    def test04(self):
        n = 4
        Output= 70
        self.assertEqual(Output,get_sol().countVowelStrings(n))
    def test05(self):
        n = 5
        Output= 126
        self.assertEqual(Output,get_sol().countVowelStrings(n))
    def test06(self):
        n = 6
        Output= 210
        self.assertEqual(Output,get_sol().countVowelStrings(n))
    def test07(self):
        n = 7
        Output= 330
        self.assertEqual(Output,get_sol().countVowelStrings(n))
    def test08(self):
        n = 8
        Output= 495
        self.assertEqual(Output,get_sol().countVowelStrings(n))
    def test09(self):
        n = 33
        Output= 66045
        self.assertEqual(Output,get_sol().countVowelStrings(n))
