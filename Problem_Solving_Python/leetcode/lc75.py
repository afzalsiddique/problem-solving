# https://www.youtube.com/watch?v=sEQk8xgjx64
import unittest
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # The groupsare nums[0:lo]=0, nums[lo:mid]=1, nums[mid:hi+1]=unclassified, nums[hi+1:]=2.
        lo, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[mid], nums[lo] = nums[lo], nums[mid]
                lo += 1
                mid += 1
            elif nums[mid] == 1:
                mid  += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                # do not do lo+=1
                #        grp 0     grp 1    unclassified    grp2
                # case: 0,0,0,0,  1,1,1,1,     2,1,1       ,2,2,2
                # case: 0,0,0,0,  1,1,1,1,     2,1,0       ,2,2,2
                high -= 1

    ###### [1,0,1] fails with this approach
    def sortColors2(self, nums: List[int]) -> None:
        n = len(nums)
        left,right = 0, n-1
        while left<right:
            if nums[left]==1 and nums[right]==1:return
            if nums[left]==0:
                left+=1
            elif nums[right]==2:
                right-=1
            elif nums[left]==2 and nums[right]==0:
                nums[left],nums[right] = nums[right], nums[left]
                left+=1
                right-=1
            elif nums[left]==1 and nums[right]==0:
                nums[left],nums[right] = nums[right], nums[left]
                left+=1
            elif nums[left]==2 and nums[right]==1:
                nums[left],nums[right] = nums[right], nums[left]
                right-=1

class MyTestCase(unittest.TestCase):

    def test1(self):
        nums = [2,0,2,1,1,0]
        Solution().sortColors(nums)
        self.assertEqual(sorted(nums), nums)

    def test2(self):
        nums = [1,0,1]
        Solution().sortColors(nums)
        self.assertEqual(sorted(nums), nums)

    def test3(self):
        nums = [0,0,0,0,  1,1,1,1,     2,1,1       ,2,2,2]
        Solution().sortColors(nums)
        self.assertEqual(sorted(nums), nums)

    def test_4(self):
        nums = [0,0,0,0,  1,1,1,1,     2,1,0       ,2,2,2]
        Solution().sortColors(nums)
        self.assertEqual(sorted(nums), nums)