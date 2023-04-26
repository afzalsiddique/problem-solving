from collections import defaultdict;
import unittest; from typing import List; import functools

def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/tallest-billboard/discuss/204160/C%2B%2B-16-ms-DFS-%2B-memo
    def tallestBillboard(self, nums):
        EMPTY,INVALID=-2,-1
        def dfs(i,s1,s2): # please note that what we are saving in dp is not the same as what we are returning
            if i==n: return s1 if s1==s2 else float('-inf')

            # dp[i,abs(50-30)]=150 -> add length of 150 to the larger support (supports are: 50 and 30. larger is 50)
            state=(i,abs(s1-s2))
            if dp[state]==EMPTY:
                ans1=dfs(i+1,s1,s2)
                ans2=dfs(i+1,s1+nums[i],s2)
                ans3=dfs(i+1,s1,s2+nums[i])
                # we are saving what length could be added to the larger support
                best=max(ans1,ans2,ans3)-max(s1,s2)
                dp[state]=max(INVALID,best)
            if dp[state]==INVALID:
                return INVALID
            # we returning what is maximum length of the support
            return dp[state]+max(s1,s2)

        n=len(nums)
        dp=defaultdict(lambda :EMPTY)
        return dfs(0,0,0)
class Solution3:
    # https://leetcode.com/problems/tallest-billboard/discuss/203181/JavaC%2B%2BPython-DP-min(O(SN2)-O(3N2-*-N)
    def tallestBillboard(self,rods):
        dp = defaultdict(int)
        dp[0]=0
        for x in rods:
            for d, y in dp.items():
                # init state
                # ------|----- d -----|      # tall side
                # - y --|                    # low  side

                # put x to tall side
                # ------|----- d -----|---- x --|
                # - y --|
                dp[d+x] = max(dp[d+x], y )

                # put x to low side
                if d >= x:
                    # ------|----- d -----|
                    # - y --|---- x ---|
                    dp[d-x] = max(dp[d-x], y+x)
                else:
                    # ------|----- d -----|
                    # - y --|-------- x --------|
                    dp[x-d] = max(dp[x-d], y+d)
        return dp[0]
class Solution2:
    # tle. dfs
    def tallestBillboard(self, rods: List[int]) -> int:
        def helper(i,left,right,remain):
            nonlocal res
            if left==right:
                res=max(res,left)
            if i==n:
                return
            if left+right+remain<2*res:
                return
            if abs(right-left)>remain:
                return
            helper(i+1,left+rods[i],right,remain-rods[i]) # use it for left support
            helper(i+1,left,right+rods[i],remain-rods[i]) # use it for right support
            helper(i+1,left,right,remain) # do not use it for any supports

        n=len(rods)
        res=0
        helper(0,0,0,sum(rods))
        return res
class Solution3:
    # tle
    def tallestBillboard(self, rods: List[int]) -> int:
        def isOn(mask:int,i:int):
            return mask&(1<<i)
        def getNums(mask:int):
            li=[]
            for i in range(n):
                if isOn(mask,i):
                    li.append(rods[i])
            return li

        n=len(rods)
        res=float('-inf')
        for mask in range(2**n-1,-1,-1):
            nums=getNums(mask)
            if self.canPartition(nums):
                res=max(res,sum(nums)//2)
        return res


    def canPartition(self, nums: List[int]) -> bool: # leetcode 416
        @functools.lru_cache(None)
        def helper(start,target):
            if target==0:
                return True
            for i in range(start,n):
                if helper(i+1,target-nums[i]):
                    return True
            return False

        n=len(nums)
        if sum(nums)%2: return False
        return helper(0,sum(nums)//2)

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(6, get_sol().tallestBillboard([1,2,3,6]))
    def test2(self):
        self.assertEqual(10, get_sol().tallestBillboard([1,2,3,4,5,6]))
    def test3(self):
        self.assertEqual(0, get_sol().tallestBillboard([1,2]))
    def test4(self):
        self.assertEqual(1023, get_sol().tallestBillboard([1,2,4,8,16,32,64,128,256,512,50,50,50,150,150,150,100,100,100,123]))
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
