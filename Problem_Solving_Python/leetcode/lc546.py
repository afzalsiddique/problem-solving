from collections import Counter;
import unittest; from typing import List; import functools


def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/remove-boxes/discuss/101310/Java-top-down-and-bottom-up-DP-solutions
    def removeBoxes(self, boxes: List[int]) -> int:
        @functools.lru_cache(None)
        # i-> left index of the array
        # j-> right index of the array (inclusive)
        # k-> number of consecutive boxes same color as boxes[i] to the left of ith box
        def dp(i,j,k):
            if i>j:
                return 0
            if i==j:
                return (k+1)*(k+1)
            ans=float('-inf')
            ans=max(ans,(k+1)*(k+1)+dp(i+1,j,0))
            for m in range(i+1,j+1):
                if boxes[i]!=boxes[m]: continue # let boxes[i] stick around until it meets boxes[m] which is same color as boxes[i]. At this moment, boxes[i+1:m] would have been removed.
                ans=max(ans,dp(i+1,m-1,0)+dp(m,j,k+1))
            return ans

        return dp(0,len(boxes)-1,0)
class Solution2:
    # wrong
    def removeBoxes(self, boxes: List[int]) -> int:
        def func(nums:List[int]):
            if not nums: return 0
            n=len(nums)
            count=Counter(nums)
            minn=min(count,key=lambda x:count[x])
            i=0
            while i<n and nums[i]==minn:
                i+=1
            j=n-1
            while j>i and nums[j]==minn:
                j-=1
            cnt=i+(n-1-j)
            score = cnt*cnt
            while i<j:
                cnt=0
                while i<j and nums[i]==minn:
                    cnt+=1
                    i+=1
                score += cnt *cnt
                i+=1
            return score + func([x for x in nums if x!=minn])

        return func(boxes)

class Tester(unittest.TestCase):
    def test_1(self):
        self.assertEqual(23,get_sol().removeBoxes([1,3,2,2,2,3,4,3,1]))
    def test_2(self):
        self.assertEqual(9,get_sol().removeBoxes([1,1,1]))
    def test_3(self):
        self.assertEqual(1,get_sol().removeBoxes([1]))
    def test_4(self):
        self.assertEqual(15,get_sol().removeBoxes([5,8,8,4,8,5,4]))
    def test_5(self):
        self.assertEqual(18,get_sol().removeBoxes([5,8,3,8,4,8,5,7,4,2]))
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):
