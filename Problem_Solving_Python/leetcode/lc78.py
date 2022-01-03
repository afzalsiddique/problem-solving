# https://leetcode.com/problems/subsets/discuss/27281/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)
# https://leetcode.com/problems/subsets/discuss/27281/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)/26331
import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(start, path):
            res.append(path)
            for i in range(start, n):
                dfs(i+1, path+[nums[i]])

        n, res = len(nums),[]
        dfs(0,[])
        return res
class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # similar but with one more parameter
        def backtrack(start):
            res.append(comb[:])
            for i in range(start, n):
                comb.append(nums[i])
                backtrack(i+1)
                comb.pop(-1)

        n, res, comb = len(nums), [], []
        backtrack(0)
        return res
class Solution3:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def isOn(mask:int,i:int): return mask&(1<<i)
        def selectItems(mask:int):
            li=[]
            for i in range(n):
                if isOn(mask,i):
                    li.append(nums[i])
            return li
        n=len(nums)
        res=[]
        for mask in range(2**n):
            res.append(selectItems(mask))
        return res

class MyTestCase(unittest.TestCase):
    def test01(self):
        actual = sorted(get_sol().subsets([1,2,3]))
        expected = sorted([[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
        self.assertEqual(expected, actual)
    def test02(self):
        actual = sorted(get_sol().subsets([0]))
        expected = sorted([[],[0]])
        self.assertEqual(expected, actual)