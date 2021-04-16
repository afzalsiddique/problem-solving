import unittest
from typing import List

class Solution:
    # https://leetcode.com/problems/maximum-product-subarray/discuss/48302/2-Passes-scan-beats-99
    # https://leetcode.com/problems/maximum-product-subarray/discuss/48302/2-Passes-scan-beats-99/706665
    def maxProduct(self, nums: List[int]) -> int:
        product,maxx=1,float('-inf')
        for num in nums:
            product *= num
            maxx=max(maxx, product)
            if num==0:product=1
        product=1
        for num in reversed(nums):
            product*=num
            maxx = max(maxx, product)
            if num==0:product=1
        return maxx

class Solution1:
    # https://leetcode.com/problems/maximum-product-subarray/
    # https://leetcode.com/problems/maximum-product-subarray/discuss/847520/Thought-process-and-useful-strategy
    # https://www.youtube.com/watch?v=hJ_Uy2DzE08
    def maxProduct(self, nums: List[int]) -> int:
        maxx = [nums[0]]
        minn = [nums[0]]
        for i in range(1, len(nums)):
            maxx.append(max(nums[i], nums[i]*maxx[i-1], nums[i]*minn[i-1]))
            minn.append(min(nums[i], nums[i]*maxx[i-1], nums[i]*minn[i-1]))
        return max(maxx)

class Solution3:
    # https://leetcode.com/problems/maximum-product-subarray/discuss/48302/2-Passes-scan-beats-99/706665
    def maxProduct(self, nums: List[int]) -> int:
        neg ,maxx= 0,float('-inf')
        for num in nums:
            if num<0:neg+=1
        if neg==1 and len(nums)==1:return nums[0]
        if neg%2==0:
            product = 1
            for num in nums:
                product*=num
                maxx = max(maxx, product)
                if num==0:product=1
            product = 1
            for num in reversed(nums):
                product*=num
                maxx = max(maxx, product)
                if num==0:product=1
            return maxx
        else:
            product,cnt = 1,0
            for num in nums:
                if num<0:cnt+=1
                if cnt==neg:break # take all numbers upto (not including) the last negative number
                product*=num
                maxx = max(maxx, product)
                if num==0:product=1
            product,cnt = 1,0
            for num in reversed(nums):
                if num<0:cnt+=1
                if cnt==neg:break # take all numbers up to (not including) the first negative number
                product*=num
                maxx=max(maxx, product)
                if num==0:product=1
        return maxx

class MyTestCase(unittest.TestCase):
    def test_1(self):
        solution = Solution()
        nums = [2,3,-2,4]
        actual = solution.maxProduct(nums)
        expected = 6
        self.assertEqual(expected, actual)

    def test_11(self):
        solution = Solution()
        nums = [2,3,-2,4, 0, 2,3,-2,4,-5]
        actual = solution.maxProduct(nums)
        expected = 240
        self.assertEqual(expected, actual)


    def test_2(self):
        solution = Solution()
        nums = [-2,0,-1]
        actual = solution.maxProduct(nums)
        expected = 0
        self.assertEqual(expected, actual)

    def test_3(self):
        solution = Solution()
        nums = [-2]
        actual = solution.maxProduct(nums)
        expected = -2
        self.assertEqual(expected, actual)
    def test_33(self):
        solution = Solution()
        nums = [-1,-2,-3]
        actual = solution.maxProduct(nums)
        expected = 6
        self.assertEqual(expected, actual)

    def test_4(self):
        solution = Solution()
        nums = [2,-5,-2,-4,3]
        actual = solution.maxProduct(nums)
        expected = 24
        self.assertEqual(expected, actual)
    def test_5(self):
        self.assertEqual(6, Solution().maxProduct([-1,-2,-3,0]))
    def test_6(self):
        self.assertEqual(2, Solution().maxProduct([-1,0,-2,2]))
