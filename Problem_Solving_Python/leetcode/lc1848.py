import unittest
from collections import deque
from typing import List
def get_sol_obj(): return Solution()
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        val=float('inf')
        for i in range(len(nums)):
            if nums[i]==target:
                temp = abs(i-start)
                if temp<val:
                    val=temp
        return val


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
