from bisect import *;
import unittest; from typing import List;


def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/make-array-strictly-increasing/discuss/377495/Java-dp-solution-:-A-simple-change-from-Longest-Increasing-Subsequence/412456
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        def check(left, right):
            numsBetween= right - left - 1
            if numsBetween==0: return 0
            start=bisect_right(arr2, arr1[left])
            end=start+numsBetween-1
            if end<len(arr2) and arr2[end]<arr1[right]:
                return numsBetween
            return -1

        n=len(arr1)
        arr1=[float('-inf')]+arr1+[float('inf')]
        arr2=list(set(arr2)) # take unique numbers because array should be strictly increasing
        arr2.sort()
        dp=[float('inf')]*(n+2)
        dp[0]=0
        for i in range(n+2):
            for j in range(i):
                if arr1[j]<arr1[i]:
                    cnt=check(j,i)
                    if cnt==-1: continue
                    dp[i]=min(dp[i],dp[j]+cnt)
        res=dp[-1]
        return res if res!=float('inf') else -1

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual(1, get_sol().makeArrayIncreasing([1,5,3,6,7], [1,3,2,4]))
    def test02(self):
        self.assertEqual(2, get_sol().makeArrayIncreasing([1,5,3,6,7], [4,3,1]))
    def test03(self):
        self.assertEqual(-1, get_sol().makeArrayIncreasing([1,5,1,6], [3,3,6]))
    def test04(self):
        self.assertEqual(5, get_sol().makeArrayIncreasing([0,11,6,1,4,3], [5,4,11,10,1,0]))
    def test05(self):
        self.assertEqual(-1, get_sol().makeArrayIncreasing([1,5,1,6,7], [1,6,3,3]))
