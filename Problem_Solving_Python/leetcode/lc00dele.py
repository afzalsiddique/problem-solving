import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp={'a':5,'e':4,'i':3,'o':2,'u':1}
        next={'a':'aeiou','e':'eiou','i':'iou','o':'ou','u':'u'}
        def dfs(n,path):
            if n==0: return 1
            ans =0
            for letter in path:
                for letter2 in next[letter]:
                    ans += dfs(n-1,path+[letter2])
            return ans

        return dfs(n,['a','e','i','o','u'])

class tester(unittest.TestCase):
    def test01(self):
        n = 1
        Output= 5
        self.assertEqual(Output,get_sol().countVowelStrings(n))
    def test02(self):
        n = 2
        Output= 15
        self.assertEqual(Output,get_sol().countVowelStrings(n))
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
