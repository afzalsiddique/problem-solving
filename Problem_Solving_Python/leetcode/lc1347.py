from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = Counter(s)
        res = 0
        for c in t:
            if count[c] > 0:
                count[c] -= 1
            else:
                res += 1
        return res
class Solution2:
    def minSteps(self, s: str, t: str) -> int:
        c1=Counter(s)
        c2=Counter(t)
        res=0
        for c in string.ascii_lowercase:
            res+=abs(c1[c]-c2[c])
        return res//2
class Solution3:
    # wrong
    def minSteps(self, s: str, t: str) -> int:
        n=len(s)
        count_s = Counter(s)
        count_t = Counter(t)
        ans=0
        for i in range(n):
            a,b=s[i],t[i]
            if a==b: continue
            if count_s[a]<=count_t[a]: continue
            count_s[a]-=1
            count_t[b]-=1
            ans+=1
        return ans

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(1,get_sol().minSteps("bab","aba"))
    def test02(self):
        self.assertEqual(5,get_sol().minSteps("leetcode","practice"))
    def test03(self):
        self.assertEqual(0,get_sol().minSteps("anagram","mangaar"))
    def test04(self):
        self.assertEqual(0,get_sol().minSteps("xxyyzz","xxyyzz"))
    def test05(self):
        self.assertEqual(4,get_sol().minSteps("friend","family"))
    def test06(self):
        self.assertEqual(18,get_sol().minSteps("gctcxyuluxjuxnsvmomavutrrfb","qijrjrhqqjxjtprybrzpyfyqtzf"))