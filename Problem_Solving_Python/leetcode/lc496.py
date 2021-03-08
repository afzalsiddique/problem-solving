import unittest
from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # index based. useful in "nextGreaterElement-ii".
        nxt,st = [-1]*len(nums2),[]
        for i in range(len(nums2)):
            while st and nums2[i]>=nums2[st[-1]]:
                top = st.pop()
                nxt[top] = nums2[i]
            st.append(i)
        index={}
        for i,num in enumerate(nums2):
            index[num]=i
        next_greater = []
        for num in nums1:
            next_greater.append(nxt[index[num]])
        return next_greater

        # element based
        st,di,nxt=[],{},[]
        for num in nums2:
            while st and num>st[-1]:
                top = st.pop()
                di[top] = num
            st.append(num)
        for num in nums1:
            if num in di:
                nxt.append(di[num])
            else:
                nxt.append(-1)
        return nxt

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.nextGreaterElement([13,7,6,12,10],[13,7,6,12,10])
        expected = [-1,12,12,-1,-1]
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.nextGreaterElement( nums1 = [2,4], nums2 = [1,2,3,4])
        expected = [3,-1]
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        actual = sol.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2])
        expected = [-1,3,-1]
        self.assertEqual(expected, actual)
