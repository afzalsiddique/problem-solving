from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
# https://www.youtube.com/watch?v=LPFhl65R7ww
class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        if len(A)>len(B):return self.findMedianSortedArrays(B, A)
        A=[float('-inf')]+A+[float('inf')] # remove this part. coz it makes complexity O(max(m,n))
        B=[float('-inf')]+B+[float('inf')]
        n1 = len(A)
        n2 = len(B)
        lo = 1
        hi  = n1-1

        while lo<=hi:
            mid1 = (lo+hi)//2
            mid2 = (n1+n2)//2-mid1 # extra element in right side when n1+n2 is odd. return min(x2,y2)
            # mid2 = (n1+n2+1)//2-mid1 # extra element in left side when n1+n2 is odd. return max(x1,y1)
            x1 = A[mid1 - 1]
            x2 = A[mid1]

            y1 = B[mid2 - 1]
            y2 = B[mid2]

            if x1 <= y2 and y1 <= x2:
                if (n1+n2)%2==0:
                    return (max(x1,y1)+min(x2,y2))/2
                else:
                    return min(x2,y2)
                    # return max(x1,y1)
            elif x1 > y2:
                hi = mid1-1
            else:
                lo = mid1+1
class Solution2:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        if len(A)>len(B):return self.findMedianSortedArrays(B, A)
        n1 = len(A)
        n2 = len(B)
        lo = 0
        hi  = n1 # !!! need to set as n1 and not "n1-1", because this means number of elements on the left side or right side, not the index

        while lo<=hi:
            mid1 = (lo+hi)//2
            mid2 = (n1+n2+1)//2-mid1 # here +1 is for taking one extra element in the left side when n1+n2 is odd

            # Why "else float('-inf')" and similarly others?
            # -> Run this case: [1,2,3,4], [5,6,7,8]
            # these are used to satisfy the conditions "x1 <= y2 and y1 <= x2"
            # -INF 0 1 2 3 4 5 +INF
            # -INF 0 1 2 3 4 5 +INF
            x1 = A[mid1 - 1] if mid1 != 0 else float('-inf')
            x2 = A[mid1] if mid1 != n1 else float('inf')

            y1 = B[mid2 - 1] if mid2 != 0 else float('-inf')
            y2 = B[mid2] if mid2 != n2 else float('inf')

            if x1 <= y2 and y1 <= x2:
                if (n1+n2)%2==0:
                    return (max(x1,y1)+min(x2,y2))/2
                else:
                    return max(x1,y1)
            elif x1 > y2:
                hi = mid1-1
            else:
                lo = mid1+1


class Solution3:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x= len(nums1)
        y = len(nums2)
        if x>y:
            nums1, nums2 = nums2, nums1
            x, y = y, x
        low = 0
        high = x
        while True:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX
            if partitionX==0:
                maxLeftX = float('-inf')
            else:
                maxLeftX = nums1[partitionX - 1]
            if partitionX == x:
                minRightX = float('inf')
            else:
                minRightX = nums1[partitionX]

            if partitionY==0:
                maxLeftY = float('-inf')
            else:
                maxLeftY = nums2[partitionY - 1]
            if partitionY == y:
                minRightY = float('inf')
            else:
                minRightY = nums2[partitionY]
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (x+y) %2:
                    return max(maxLeftX, maxLeftY)
                else:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            elif maxLeftX > minRightY:
                high = partitionX - 1
            else:
                low = partitionX + 1
class MyTestClass(unittest.TestCase):
    def test01(self):
        nums1 = [1]
        nums2 = [7,11,18,19,21,25]
        actual = get_sol().findMedianSortedArrays(nums1, nums2)
        expected = 18
        self.assertEqual(expected, actual)
    def test02(self):
        nums1 = [1,2,3,4]
        nums2 = [5,6,7,8]
        actual = get_sol().findMedianSortedArrays(nums1, nums2)
        expected = 4.5
        self.assertEqual(expected, actual)
    def test03(self):
        nums1 = [1,3,8,9,15]
        nums2 = [7,11,18,19,21,25]
        actual = get_sol().findMedianSortedArrays(nums1, nums2)
        expected = 11
        self.assertEqual(expected, actual)
    def test04(self):
        nums1 = [0,0]
        nums2 = [0,0]
        actual = get_sol().findMedianSortedArrays(nums1, nums2)
        expected = 0.0
        self.assertEqual(expected, actual)
    def test05(self):
        self.assertEqual(1.0,get_sol().findMedianSortedArrays([], [1]))