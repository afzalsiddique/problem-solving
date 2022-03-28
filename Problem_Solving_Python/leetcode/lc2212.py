from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        def calculateScore(bobArrows):
            ans=0
            for i in range(12):
                if bobArrows[i]>aliceArrows[i]:
                    ans+=i
            return ans
        def backtrack(i,path):
            nonlocal res,bobArrows
            if i==n:
                score=calculateScore(path)
                if score>res:
                    res=score
                    bobArrows=path
                return
            if numArrows-sum(path)>=aliceArrows[i]+1:
                backtrack(i+1,path+[aliceArrows[i]+1])
            backtrack(i+1,path+[0])

        n=len(aliceArrows)
        res=float('-inf')
        bobArrows=[]
        backtrack(0,[])
        bobArrows[0]+=numArrows-sum(bobArrows)
        return bobArrows

class tester(unittest.TestCase):
    def test01(self):
        self.assertEqual([0,0,0,0,1,1,0,0,1,2,3,1],get_sol().maximumBobPoints( 9, [1,1,0,1,0,0,2,1,0,1,2,0]))
    def test02(self):
        self.assertEqual( [0,0,0,0,0,0,0,0,1,1,1,0] ,get_sol().maximumBobPoints(3, [0,0,1,0,0,0,0,0,0,0,0,2]))
    def test03(self):
        self.assertEqual( [21,3,0,2,8,2,17,8,4,14,4,6] ,get_sol().maximumBobPoints(89, [3,2,28,1,7,1,16,7,3,13,3,5]))

