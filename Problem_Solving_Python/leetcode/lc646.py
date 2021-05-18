import itertools
import math
import operator
import random
from bisect import *
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
def get_sol(): return Solution()

class Solution:
    # greedy
    # time O(nlogn) space O(1)
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=operator.itemgetter(1)) # sort based on 1 index
        b=float('-inf')
        cnt=0
        for pair in pairs:
            c = pair[0]
            if c>b:
                cnt+=1
                b=pair[1]
        return cnt
class Solution2:
    # greedy
    # time O(nlogn) space O(n)
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=operator.itemgetter(1)) # sort based on 1 index
        res=[[-2001,-2000]] # dummy
        for pair in pairs:
            b = res[-1][1]
            c = pair[0]
            if c>b: res.append(pair)
        return len(res)-1
class Solution3:
    # longest incresing subsequence
    # time O(n^2) space O(n^2)
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n=len(pairs)
        pairs.sort(key=operator.itemgetter(1))
        lis = [1]*n
        for i in range(n):
            for j in range(i):
                b=pairs[j][1]
                c=pairs[i][0]
                if c>b:
                    lis[i]=max(lis[i],lis[j]+1)
        return max(lis)

class mytestcase(unittest.TestCase):
    def test1_1(self):
        pairs = [[1,2],[2,3],[3,4]]
        Output= 2
        self.assertEqual(Output,get_sol().findLongestChain(pairs))
    def test1_2(self):
        pairs = [[1,2],[7,8],[4,5]]
        Output= 3
        self.assertEqual(Output,get_sol().findLongestChain(pairs))
