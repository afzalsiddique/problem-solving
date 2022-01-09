import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
# from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=nxQsb2mVdHs&t=495s
    def minCost(self, n: int, cuts: List[int]) -> int:
        @functools.lru_cache(None)
        def backtrack(left, right):
            if right-left<=1:
                return 0
            ans=float('inf')
            for i in range(left+1,right):
                part1= backtrack(left, i)
                part2= backtrack(i, right)
                tmp=part1+part2+cuts[right]-cuts[left]
                ans=min(ans,tmp)
            return ans

        cuts.append(0)
        cuts.append(n)
        cuts.sort()
        return backtrack(0, len(cuts) - 1)
class Solution2:
    # tle
    def minCost(self, n: int, cuts: List[int]) -> int:
        @functools.lru_cache(None)
        def refineCuts(left:int,right:int,cuts:tuple[int]):
            cuts=list(cuts)
            li=[]
            for i in range(len(cuts)):
                if left<cuts[i]<right:
                    li.append(cuts[i])
            return tuple(li)
        @functools.lru_cache(None)
        def backtrack(left,right,cuts:tuple[int]):
            ans=float('inf')
            for c in cuts:
                part1=backtrack(left,c,refineCuts(left,c,cuts))
                part2=backtrack(c,right,refineCuts(c,right,cuts))
                tmp=part1+part2+right-left
                ans=min(ans,tmp)
            if ans==float('inf'):
                ans=0
            return ans

        return backtrack(0,n,tuple(cuts))


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(16, get_sol().minCost(7, [1,3,4,5]))
    def test2(self):
        self.assertEqual(22, get_sol().minCost( 9, [5,6,1,4,2]))
    def test3(self):
        self.assertEqual(14, get_sol().minCost(7, [1,3,4]))
    def test4(self):
        self.assertEqual(127, get_sol().minCost(30, [13,25,16,20,26,5,27,8,23,14,6,15,21,24,29,1,19,9,3]))
    def test5(self):
        self.assertEqual(4854, get_sol().minCost(774, [174,726,424,757,53,706,364,8,429,163,290,476,245,454,480,197,139,208,301,568,241,246,592,162,170,89,591,341,548,574,611,100,105,274,270,83,461,492,652,177,702,338,69,273,59,741,442,184,294,210,394,230,576,392,34,192,734,78,16,604,285,282,550,388,351,503,629,526,131,508,662,374,497,123,470,520,430,637,561,133,617,334,642,577,466,699,306,300,304,42,398,344,521,661]))
    def test6(self):
        self.assertEqual(3971, get_sol().minCost(655, [361,132,484,271,509,401,5,181,420,6,254,13,10,134,610,108,275,593,277,394,101,267,333,248,232,474,56,304,523,543,295,143,171,299,130,512,448,180,629,294,502,384,82,35,164,496,620,40,637,352,513,374,450,25,195,43,276,398,414,20,337,38,331,380,559,278,241,291,468,422,454,7,67,596,259,614,27,636,647,208,272,106,541,377,530,451]))
    def test7(self):
        self.assertEqual(33, get_sol().minCost(15, [8,10,4,11]))
    def test8(self):
        self.assertEqual(245, get_sol().minCost(68, [15,19,12,43,63,35,33,21,58,37,11,5,45]))
    def test9(self):
        self.assertEqual(168, get_sol().minCost(68, [43,63,35,33,21]))
