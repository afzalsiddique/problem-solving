import unittest
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        j=0
        flag = False
        for i in range(1, n):
            if nums[i]==nums[j]:
                nums[j+1] = nums[i]
                flag = True
                if j+1!=i:nums[i]='ignore'
            else:
                if j+2<n and nums[j] == nums[j+1]:
                    nums[j+2] = nums[i]
                    if j+2!=i:nums[i]='ignore'
                    j+=2
                elif nums[i]!=nums[j]:
                    nums[j+1] = nums[i]
                    if j+1!=i:nums[i]='ignore'
                    j+=1
                flag = False
        if flag:
            return j+2
        return j+1

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.removeDuplicates([1,1,1,2,3])
        expected = None
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.removeDuplicates([0,0,1,1,1,1,2,3,3])
        expected = None
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        actual = sol.removeDuplicates(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        actual = sol.removeDuplicates(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        actual = sol.removeDuplicates(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        actual = sol.removeDuplicates(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        actual = sol.removeDuplicates(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        actual = sol.removeDuplicates(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        actual = sol.removeDuplicates(0)
        expected = 0
        self.assertEqual(expected, actual)