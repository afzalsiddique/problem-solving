import unittest
from typing import List
# impossibilities
# 1. using a dictionary (key,value) = (current element, next greater element). because there might be duplicates values
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result,stack = [-1]*len(nums),[]
        n = len(nums)
        # index based helps with duplicates
        # loop twice
        for i in range(n):
            while stack and nums[i]>nums[stack[-1]]:
                top = stack.pop()
                result[top] = nums[i]
            stack.append(i)
        for i in range(n):
            while stack and nums[i]>nums[stack[-1]]:
                top = stack.pop()
                result[top] = nums[i]
            if stack == []: # performance increase and nothing else
                break
            stack.append(i)

        return result

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        nums=[13,7,6,10,11,15,16,14,3,12,1]
        actual = sol.nextGreaterElements(nums)
        expected = [15,10,10,11,15,16,-1,15,12,13,13]
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        nums=[1,2,1]
        actual = sol.nextGreaterElements(nums)
        expected = [2,-1,2]
        self.assertEqual(expected, actual)
    def test_4(self):
        sol = Solution()
        nums=[1,1,1,1,1]
        actual = sol.nextGreaterElements(nums)
        expected = [-1,-1,-1,-1,-1]
        self.assertEqual(expected, actual)
    def test_5(self):
        sol = Solution()
        nums=[1,2,3,4]
        actual = sol.nextGreaterElements(nums)
        expected = [2,3,4,-1]
        self.assertEqual(expected, actual)
    def test_6(self):
        sol = Solution()
        nums=[4,3,2,1]
        actual = sol.nextGreaterElements(nums)
        expected = [-1,4,4,4]
        self.assertEqual(expected, actual)
    def test_7(self):
        sol = Solution()
        nums=[100,1,11,1,120,111,123,1,-1,-100]
        actual = sol.nextGreaterElements(nums)
        expected = [120,11,120,120,123,123,-1,100,100,100]
        self.assertEqual(expected, actual)
# nums=[13,7,6,12,10]
# print(nextGreaterElements(nums),[-1,12,12,13,13])
# print(nextGreaterElements(nums))
# print([15,10,10,11,15,16,-1,15,12,13,13])
