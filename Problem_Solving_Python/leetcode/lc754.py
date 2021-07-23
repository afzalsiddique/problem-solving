import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/reach-a-number/discuss/112968/Short-JAVA-Solution-with-Explanation
    # math
    def reachNumber(self, target: int) -> int:
        step=0
        cum_sum=0
        target=abs(target)
        while cum_sum<target:
            step+=1
            cum_sum+=step
        while (cum_sum-target)%2:
            step+=1
            cum_sum+=step
        return step
class Solution2:
    # bfs tle
    def reachNumber(self, target: int) -> int:
        step=1
        q=deque([0])
        while q:
            for _ in range(len(q)):
                curr=q.popleft()
                if curr==target:
                    return step-1
                q.append(curr+step)
                q.append(curr-step)
            step+=1


class tester(unittest.TestCase):
    def test_1(self):
        target = 2
        Output= 3
        self.assertEqual(Output,get_sol().reachNumber(target))
    def test_2(self):
        target = 3
        Output= 2
        self.assertEqual(Output,get_sol().reachNumber(target))
    def test_3(self):
        target = -2
        Output= 3
        self.assertEqual(Output,get_sol().reachNumber(target))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
