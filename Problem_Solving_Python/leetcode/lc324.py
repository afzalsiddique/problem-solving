import unittest
from collections import deque
from typing import List
def get_sol_obj(): return Solution()
class Solution:
    # https://leetcode.com/problems/wiggle-sort-ii/discuss/155764/Python-3-lines-simplest-solution-for-everyone-to-understand
    # bad solution
    # time O(n log n) space (n)
    def wiggleSort(self, nums: List[int]) -> None:
        n=len(nums)
        res = sorted(nums)
        i=n-1
        for idx in range(1,n,2):
            nums[idx]=res[i]
            i-=1
        i=0
        for idx in reversed(range(0,n,2)):
            nums[idx]=res[i]
            i+=1
class tester(unittest.TestCase):
    def test1(self):
        nums = [1,5,1,1,6,4]
        Output= [1,6,1,5,1,4]
        get_sol_obj().wiggleSort(nums)
        self.assertEqual(Output,nums)
    def test2(self):
        nums = [1,3,2,2,3,1]
        Output= [2,3,1,3,1,2]
        get_sol_obj().wiggleSort(nums)
        self.assertEqual(Output,nums)
    def test3(self):
        nums = [4,5,5,6]
        Output= [5,6,4,5]
        get_sol_obj().wiggleSort(nums)
        self.assertEqual(Output,nums)
