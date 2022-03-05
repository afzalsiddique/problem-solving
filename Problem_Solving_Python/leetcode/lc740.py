from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def deleteAndEarn(self, A: List[int]) -> int:
        @cache
        def dp(i):
            if i==n:
                return 0
            option1=A[i]*count[A[i]]+dp(bisect_right(A,A[i]+1))
            # option1=A[i]*(bisect_right(A,A[i])-bisect_left(A,A[i])) +dp(bisect_right(A,A[i]+1)) # count not required
            option2=dp(bisect_right(A,A[i]))
            return max(option1,option2)

        n=len(A)
        count=Counter(A)
        A.sort()
        return dp(0)
class Solution2:
    # time O(n)
    # space O(n) for creating gold array otherwise space O(1)
    def deleteAndEarn(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1: return nums[0]
        BIG = 20001
        gold = [0]*BIG
        for num in nums:
            gold[num]+=num
        second_last=gold[0]
        last=max(gold[0],gold[1])
        for i in range(2,BIG):
            cur = max(gold[i]+second_last, last)
            second_last=last
            last=cur
        return max(last,second_last)


class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(6,get_sol().deleteAndEarn([3,4,2]))
    def test02(self):
        self.assertEqual(9,get_sol().deleteAndEarn([2,2,3,3,3,4]))