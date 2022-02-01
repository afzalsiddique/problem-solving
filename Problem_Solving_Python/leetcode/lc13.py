from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def romanToInt(self, s: str) -> int:
        n=len(s)
        val={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        nxt = {'I':'VX','X':'LC','C':'DM','V':'','L':'','D':'','M':''}
        res=0
        for i in range(n):
            if i<n-1 and s[i+1] in nxt[s[i]]:
                res-=val[s[i]]
            else:
                res+=val[s[i]]
        return res
class Solution2:
    def romanToInt(self, s: str) -> int:
        value = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        di = defaultdict(str)
        di['I'] = 'VX'
        di['X'] = 'LC'
        di['C'] = 'DM'
        di['dummy'] = ''
        last = 'dummy'
        ans = 0
        for c in s:
            ans += value[c]
            if c in di[last]:
                ans -= 2*value[last]
            last = c
        return ans
class Solution3:
    def romanToInt2(self, s: str) -> int:
        val = {'I':1, 'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'Z':0}
        di = {'I':'VX','X':'LC','C':'DM','V':'','L':'','D':'','M':'','Unknown':'IVXLCDM'}
        last = 'Unknown'
        ans = 0
        for ch in s:
            if ch in di[last]:
                ans += val[ch] - 2 * val[last]
            else:
                ans += val[ch]
            last = ch
        return ans

class tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(3,get_sol().romanToInt("III"))
    def test02(self):
        self.assertEqual(58,get_sol().romanToInt("LVIII"))
    def test03(self):
        self.assertEqual(1994,get_sol().romanToInt("MCMXCIV"))
