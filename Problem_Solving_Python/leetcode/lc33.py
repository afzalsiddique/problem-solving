import unittest
from bisect import bisect_left
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:return mid
            if r-l+1 ==1 or r-l+1==2 or r-l+1==3:
                if nums[l]==target: return l
                elif nums[r]==target: return r
                else: return -1
            if nums[l]<nums[mid]:
                if nums[l]<=target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if nums[mid]<target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
        return -1

    def search2(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            mid = l+(r-l)//2
            if nums[mid]==target:
                return mid
            if nums[mid] <nums[r]:
                if nums[mid] < target <=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
            else:
                if nums[l]<=target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
        return -1
    def search_v2(self, nums: List[int], target: int) -> int:
        n=len(nums)
        lo,hi=0,n-1
        while lo<=hi:
            mid=(lo+hi)//2

            if nums[mid]==target:
                return mid

            if nums[lo]<=nums[mid]:
                if nums[lo]<=target<=nums[mid]:
                    idx=bisect_left(nums,target,lo,hi)
                    return idx if idx!=n and nums[idx]==target else -1
                else:
                    lo=mid+1
            elif nums[mid]<=nums[hi]:
                if nums[mid]<=target<=nums[hi]:
                    idx=bisect_left(nums,target,lo,hi)
                    return idx if idx!=n and nums[idx]==target else -1
                else:
                    hi=mid-1
        return -1



class MyTestCase(unittest.TestCase):

    def test_1(self):
        expected = 4
        actual = Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=0)
        self.assertEqual(expected, actual)

    def test_2(self):
        expected = -1
        actual = Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=3)
        self.assertEqual(expected, actual)
    def test_3(self):
        expected = -1
        actual = Solution().search(nums=[1], target=0)
        self.assertEqual(expected, actual)

    def test_4(self):
        expected = 0
        actual = Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=4)
        self.assertEqual(expected, actual)

    def test_5(self):
        expected = 6
        actual = Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=2)
        self.assertEqual(expected, actual)

    def test_6(self):
        expected = 2
        actual = Solution().search(nums=[5, 6, 4], target=4)
        self.assertEqual(expected, actual)

    def test_7(self):
        expected = 1
        actual = Solution().search(nums=[4, 5, 6], target=5)
        self.assertEqual(expected, actual)

    def test_8(self):
        expected = 2
        actual = Solution().search(nums=[4, 5, 6], target=6)
        self.assertEqual(expected, actual)

    def test_9(self):
        expected = 0
        actual = Solution().search(nums=[4, 5], target=4)
        self.assertEqual(expected, actual)

    def test_10(self):
        expected = 0
        actual = Solution().search(nums=[5, 4], target=5)
        self.assertEqual(expected, actual)

    def test_11(self):
        expected = -1
        actual = Solution().search([1, 3, 5], 2)
        self.assertEqual(expected, actual)

    def test_12(self):
        expected = 0
        actual = Solution().search([5, 1, 3], 5)
        self.assertEqual(expected, actual)

    def test_13(self):
        expected = 1
        actual = Solution().search([1, 3], 3)
        self.assertEqual(expected, actual)
    def test_14(self):
        expected = 0
        actual = Solution().search([6,7,1,2,3,4,5], 6)
        self.assertEqual(expected, actual)
    def test_15(self):
        expected = 1
        actual = Solution().search([3,1], 1)
        self.assertEqual(expected, actual)
