# https://leetcode.com/problems/single-element-in-a-sorted-array/discuss/627921/Java-or-C%2B%2B-or-Python3-or-Easy-explanation-or-O(logn)-or-O(1)
# https://leetcode.com/problems/single-element-in-a-sorted-array/discuss/627786/C++-O(log-n)-time-O(1)-space-or-Simple-and-clean-or-Use-xor-to-keep-track-of-odd-even-pair/537615
import unittest
from typing import List


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

    def test_0(self):
        sol = Solution()
        expected = 1
        actual = sol.singleNonDuplicate([1,2,2])
        self.assertEqual(expected, actual)
    def test_1(self):
        sol = Solution()
        expected = 2
        actual = sol.singleNonDuplicate([1,1,2,3,3,4,4,8,8])
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        expected = 10
        actual = sol.singleNonDuplicate([3,3,7,7,10,11,11])
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        expected = 2
        actual = sol.singleNonDuplicate([0,0,1,1,2,3,3,4,4,5,5,6,6])
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        expected = 2
        actual = sol.singleNonDuplicate([0,0,1,1,2,3,3,4,4,5,5,6,6])
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        expected = 4
        actual = sol.singleNonDuplicate([0,0,1,1,2,2,3,3,4,5,5])
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        expected = 0
        actual = sol.singleNonDuplicate([0,1,1,2,2,3,3,4,4,5,5])
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        expected = 6
        actual = sol.singleNonDuplicate([1,1,2,2,3,3,4,4,5,5,6])
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        expected = 1
        actual = sol.singleNonDuplicate([1,2,2])
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        expected = 2
        actual = sol.singleNonDuplicate([1,1,2])
        self.assertEqual(expected, actual)

    def test_10(self):
        sol = Solution()
        expected = 3
        actual = sol.singleNonDuplicate([1,1,2,2,3])
        self.assertEqual(expected, actual)

    def test_11(self):
        sol = Solution()
        expected = 1
        actual = sol.singleNonDuplicate([1])
        self.assertEqual(expected, actual)