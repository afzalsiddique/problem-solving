# https://www.youtube.com/watch?v=quAS1iydq7U
import unittest
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1. Find the largest index k such that nums[k] < nums[k + 1].If no such index exists, just reverse nums and done.
        # 2. Find the largest index l > k such that nums[k] < nums[l].
        # 3. Swap nums[k] and nums[l].
        # 4. Reverse the sub - array nums[k + 1:].
        
        n = len(nums)

        k = 'not found'
        # step 1a
        i = n - 1
        while i >= 0:
            if i < n - 1 and nums[i] < nums[i + 1]:
                k = i
                break
            i -= 1

        # step 1b
        if k == 'not found':
            nums.reverse()
            return

        # step 2:
        i = n - 1
        while i >= 0:
            if nums[i] > nums[k]:
                # step 3
                nums[i], nums[k] = nums[k], nums[i]
                break
            i -= 1

        # step 4
        right = n - 1
        left = k + 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        nums = [1,3,5,4,2]
        solution.nextPermutation(nums)
        expected = [1,4,2,3,5]
        self.assertEqual(expected, nums)

    def test_2(self):
        solution = Solution()
        nums = [1,1,5]
        solution.nextPermutation(nums)
        expected = [1,5,1]
        self.assertEqual(expected, nums)

    def test_3(self):
        solution = Solution()
        nums = [3,2,1]
        solution.nextPermutation(nums)
        expected = [1,2,3]
        self.assertEqual(expected, nums)

    def test_4(self):
        solution = Solution()
        nums = [1,2,3]
        solution.nextPermutation(nums)
        expected = [1,3,2]
        self.assertEqual(expected, nums)

    def test_5(self):
        solution = Solution()
        nums = [1]
        solution.nextPermutation(nums)
        expected = [1]
        self.assertEqual(expected, nums)

    def test_6(self):
        solution = Solution()
        nums = [1,3,2]
        solution.nextPermutation(nums)
        expected = [2,1,3]
        self.assertEqual(expected, nums)

    def test_7(self):
        solution = Solution()
        nums = [1,5,1]
        solution.nextPermutation(nums)
        expected = [5,1,1]
        self.assertEqual(expected, nums)

    def test_8(self):
        solution = Solution()
        nums = [6,2,1,5,4,3,0]
        solution.nextPermutation(nums)
        expected = [6,2,3,0,1,4,5]
        self.assertEqual(expected, nums)

    def test_9(self):
        solution = Solution()
        nums = [6,2,1,5,4,3,3,0]
        solution.nextPermutation(nums)
        expected = [6,2,3,0,1,3,4,5]
        self.assertEqual(expected, nums)

    def test_10(self):
        solution = Solution()
        nums = [6,2,1,5,5,4,3,0]
        solution.nextPermutation(nums)
        expected = [6,2,3,0,1,4,5,5]
        self.assertEqual(expected, nums)