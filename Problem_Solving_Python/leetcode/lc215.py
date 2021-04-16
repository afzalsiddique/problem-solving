# https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/762174/4-python-solutions-with-step-by-step-optimization-plus-time-and-space-analysis
import unittest
from typing import List
from random import uniform
# quick select average O(n) time and O(1) space
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or not k or k < 0:
            return None
        return self.quick_select(nums, k, 0, len(nums) - 1)

    def quick_select(self, nums, k, start, end):
        l, r = start, end
        mid = l + (r - l) // 2
        pivot = nums[mid]
        while l <= r:
            while l <= r and nums[l] > pivot:
                l += 1
            while l <= r and nums[r] < pivot:
                r -= 1

            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        if start + k - 1 <= r:
            return self.quick_select(nums, k, start, r)
        if start + k - 1 >= l:
            return self.quick_select(nums, k - (l - start), l, end)
        return nums[r + 1]

# quick select. average O(n). space O(n)
class Solution4:
    def findKthLargest(self, nums, k):
        pivot = nums[0]
        left  = [l for l in nums if l < pivot]
        equal = [e for e in nums if e == pivot]
        right = [r for r in nums if r > pivot]

        if k <= len(right):
            return self.findKthLargest(right, k)
        elif (k - len(right)) <= len(equal):
            return equal[0]
        else:
            return self.findKthLargest(left, k - len(right) - len(equal))
class Solution6:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # transform into the k smallest
        k = len(nums)-k
        # solve kth smallest in O(n)
        def quick_select(nums, k):
            # get a random pivot
            pivot = int(uniform(0, len(nums)))
            # smaller than pivot -> left, bigger -> right
            left, right = [], []
            for i, e in enumerate(nums):
                if e <= nums[pivot] and i != pivot: left.append(e)
                if e > nums[pivot]: right.append(e)
            # match with k, we are done
            if k == len(left): return nums[pivot]
            # keep exploring
            if k < len(left):
                return quick_select(left, k)
            else:
                return quick_select(right, k-len(left)-1)
        return quick_select(nums, k)
# quick select. but worst case is n^2
class Solution3:
    def findKthLargest(self, nums, k):
        def quickSelect(left, right): # quick select
            pos = partition(left, right)
            if pos == k-1:
                return nums[pos]
            elif pos >= k: # '>=' because nums is 0 indexed but k is 1 indexed
                return quickSelect(left, pos - 1)
            return quickSelect(pos + 1, right)

        def partition(left, right):
            pivot = nums[right] # pick the last one as pivot
            i = left
            for j in range(left, right): # left to right -1. nums[right] is pivot so exclude that.
                if nums[j] > pivot: # the larger elements are in left side
                    nums[j], nums[i] = nums[i], nums[j]
                    i += 1
            nums[right], nums[i] = nums[i], nums[right] # swap the i and the last element
            return i


        return quickSelect(0, len(nums)-1)

# merge sort
class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.mergeSort(nums)
        return nums[k-1]

    def mergeSort(self, nums):
        if len(nums) > 1:
            mid = len(nums) // 2
            L = nums[:mid]
            R = nums[mid:]
            self.mergeSort(L)
            self.mergeSort(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i]> R[j]:
                    nums[k] = L[i]
                    i += 1
                else:
                    nums[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                nums[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                nums[k] = R[j]
                j += 1
                k += 1



class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(5, Solution().findKthLargest([3,2,1,5,6,4], k = 2))
    def test_2(self):
        self.assertEqual(4, Solution().findKthLargest([3,2,3,1,2,4,5,5,6], k = 4))
    def test_3(self):
        self.assertEqual(5, Solution().findKthLargest([3,2,1,5,6,4], k = 2))
