from itertools import accumulate; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *; from a_linked_list import make_linked_list
def get_sol(): return Solution()

class Solution:
    # https://www.youtube.com/watch?v=sEQk8xgjx64
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

class Solution2:
    def sortColors(self, A: List[int]) -> None:
        def swap(i,j): A[i],A[j]=A[j],A[i]
        n=len(A)
        zero=0 # points to num after all the zeros
        one=zero # points to num after all the ones
        two=n-1 # points to num before all the twos

        while one<=two:
            if A[zero]==0:
                zero+=1
            elif A[one]==1:
                one+=1
            elif A[two]==2:
                two-=1
            elif A[one]==0:
                swap(zero,one)
            elif A[two]==0:
                swap(zero,two)
            elif A[two]==1:
                swap(one,two)
            one=max(zero,one) # all ones should be after all zeros
class Solution3:
    ###### [1,0,1] fails with this approach
    def sortColors(self, nums: List[int]) -> None:
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
    def test01(self):
        nums = [2,0,2,1,1,0]
        get_sol().sortColors(nums)
        self.assertEqual(sorted(nums), nums)
    def test02(self):
        nums = [1,0,1]
        get_sol().sortColors(nums)
        self.assertEqual(sorted(nums), nums)
    def test03(self):
        nums = [0,0,0,0,  1,1,1,1,     2,1,1       ,2,2,2]
        get_sol().sortColors(nums)
        self.assertEqual(sorted(nums), nums)
    def test04(self):
        nums = [0,0,0,0,  1,1,1,1,     2,1,0       ,2,2,2]
        get_sol().sortColors(nums)
        self.assertEqual(sorted(nums), nums)
    def test05(self):
        nums = [1,0,1]
        get_sol().sortColors(nums)
        self.assertEqual(sorted(nums), nums)
    def test06(self):
        nums = [2,0,1]
        get_sol().sortColors(nums)
        self.assertEqual(sorted(nums), nums)
