import unittest
from typing import List

# Boyer Moore
# https://www.youtube.com/watch?v=gY-I8uQrCkk
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = nums[0], 0
        for num in nums:
            if num==candidate:
                count+=1
            else:
                count-=1
                if count==0:
                    candidate=num
                    count+=1
        return candidate

class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 0
        for i in range(len(nums)):
            if count ==0:
                candidate=nums[i]
                count=1
            elif nums[i]==candidate:
                count+=1
            else:
                count-=1
        return candidate
class Solution3:
    def majorityElement(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums))[0]

    def helper(self, nums, l, r):
        if l == r - 1:
            return nums[l], 1
        mid = l + (r - l) // 2
        maj_left, extra_left = self.helper(nums, l, mid)
        maj_right, extra_right = self.helper(nums, mid, r)

        if maj_right==maj_left:
            maj = maj_left
            extra = extra_left + extra_right
        elif extra_right > extra_left:
            maj = maj_right
            extra = extra_right - extra_left
        else:
            maj = maj_left
            extra = extra_left - extra_right
        return maj, extra

class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        nums = [3,2,3]
        actual = solution.majorityElement(nums)
        expected = 3
        self.assertEqual(expected, actual)

    def test_2(self):
        solution = Solution()
        nums = [2,2,1,1,1,2,2]
        actual = solution.majorityElement(nums)
        expected = 2
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        nums = [6,5,5]
        actual = solution.majorityElement(nums)
        expected = 5
        self.assertEqual(expected, actual)


