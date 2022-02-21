from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
# https://leetcode.com/problems/single-element-in-a-sorted-array/discuss/627921/Java-or-C%2B%2B-or-Python3-or-Easy-explanation-or-O(logn)-or-O(1)
# https://leetcode.com/problems/single-element-in-a-sorted-array/discuss/627786/C++-O(log-n)-time-O(1)-space-or-Simple-and-clean-or-Use-xor-to-keep-track-of-odd-even-pair/537615

class Solution:
    # https://leetcode.com/problems/single-element-in-a-sorted-array/discuss/100754/Java-Binary-Search-short-(7l)-O(log(n))-w-explanations/235525
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo,hi=0,len(nums)-1
        while lo<hi: # why it is "<"? -> because "hi=mid" and not "hi=mid-1"
            mid= (lo+hi)//2
            if mid%2==0:
                # if mid is even, then it's duplicate should be in next index.
                # or if mid is odd, then it's duplicate  should be in previous index.
                if nums[mid]==nums[mid+1]:
                    lo = mid+2
                else:
                    hi=mid
            else:
                if nums[mid]==nums[mid-1]:
                    lo = mid +1
                else:
                    hi = mid
        return nums[lo]


    def singleNonDuplicate_(self, nums: List[int]) -> int:
        lo,hi=0,len(nums)-1
        # we can observe that for each pair,
        # first element takes even position and second element takes odd position
        # Our target is to find "the first even position index which does not equal to its next element"
        while lo<hi: # why it is "<"? -> because "hi=mid" and not "hi=mid-1"
            # https://leetcode.com/problems/search-insert-position/discuss/249092/Java-solution-with-detailsexplanation-for-every-line-code
            # https://leetcode.com/problems/single-element-in-a-sorted-array/discuss/100754/Java-Binary-Search-short-(7l)-O(log(n))-w-explanations/263150
            mid= (lo+hi)//2
            if mid%2==1:
                mid-=1
            if nums[mid]!=nums[mid+1]:
                hi=mid # not "hi = mid -1". because at this point mid is still a possibility. case-> [1,1,2,3,3].
                        # This also changes the while loop condition to become "lo<hi" and not "lo<=hi".
            else:
                lo=mid+2 # because the matching value of the mid exists just after the mid. "lo = mid + 1" will should work as well
        return nums[lo]


class MyTestCase(unittest.TestCase):
    def test00(self):
        self.assertEqual(1, get_sol().singleNonDuplicate([1,2,2]))
    def test01(self):
        self.assertEqual(2, get_sol().singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
    def test02(self):
        self.assertEqual(10, get_sol().singleNonDuplicate([3,3,7,7,10,11,11]))
    def test03(self):
        self.assertEqual(2, get_sol().singleNonDuplicate([0,0,1,1,2,3,3,4,4,5,5,6,6]))
    def test04(self):
        self.assertEqual(2, get_sol().singleNonDuplicate([0,0,1,1,2,3,3,4,4,5,5,6,6]))
    def test05(self):
        self.assertEqual(4, get_sol().singleNonDuplicate([0,0,1,1,2,2,3,3,4,5,5]))
    def test06(self):
        self.assertEqual(0, get_sol().singleNonDuplicate([0,1,1,2,2,3,3,4,4,5,5]))
    def test07(self):
        self.assertEqual(6, get_sol().singleNonDuplicate([1,1,2,2,3,3,4,4,5,5,6]))
    def test08(self):
        self.assertEqual(1, get_sol().singleNonDuplicate([1,2,2]))
    def test09(self):
        self.assertEqual(2, get_sol().singleNonDuplicate([1,1,2]))
    def test10(self):
        self.assertEqual(3, get_sol().singleNonDuplicate([1,1,2,2,3]))
    def test11(self):
        self.assertEqual(1, get_sol().singleNonDuplicate([1]))