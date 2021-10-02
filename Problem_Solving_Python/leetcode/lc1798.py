import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        cur_sum = 0
        target=1
        for i in range(len(coins)):
            if coins[i]<=target<=coins[i]+cur_sum:
                cur_sum+=coins[i]
                target=cur_sum+1
            else:
                break
        return target

class Solution2:
    # tle
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        res = self.subsetsWithDup(coins)
        sett = set()
        for item in res:
            sett.add(sum(item))
        li = list(sett)
        li.sort()
        cnt = 1
        for i in range(1, len(li)):
            if li[i]!=li[i-1]+1:
                break
            cnt+=1
        return cnt
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n, res = len(nums),[]

        def dfs(start, path):
            res.append(path)

            for i in range(start, n):
                if i>start and nums[i]==nums[i-1]:continue
                dfs(i+1, path+[nums[i]])

        nums.sort()
        dfs(0,[])
        return res





class MyTestCase(unittest.TestCase):
    def test_1(self):
        a = Solution().getMaximumConsecutive([1,1,1,4])
        self.assertEqual(8, a)
    def test_2(self):
        a = Solution().getMaximumConsecutive([1,3])
        self.assertEqual(2, a)
    def test_3(self):
        a = Solution().getMaximumConsecutive([1,4,10,3,1])
        self.assertEqual(20, a)
    def test_4(self):
        a = Solution().getMaximumConsecutive([i for i in range(1,23)])
        self.assertEqual(20, a)
