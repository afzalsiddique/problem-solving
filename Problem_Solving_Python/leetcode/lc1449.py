import unittest; from typing import List; import functools


def get_sol(): return Solution()
class Solution:
    def largestNumber(self, cost, target) -> str:
        def getMax(a:str, b:str):
            if '0' in a:
                return b
            if '0' in b:
                return a
            if len(a)>len(b):
                return a
            if len(b)>len(a):
                return b
            return a if a>b else b

        @functools.lru_cache(None)
        def dfs(index, remain):
            if remain == 0:
                return ''
            elif remain < 0 or index == len(cost)+1:
                return '0'
            take = str(index) + dfs(1, remain - cost[index - 1])
            skip = dfs(index + 1, remain)
            return getMax(take, skip)

        ans = dfs(1, target)
        return ans if '0' not in ans else '0'
class Solution2:
    # https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/discuss/635267/C++JavaPython-Strict-O(Target)/544206
    def largestNumber(self, cost, target)->str:
        dp=[float('-inf')]*(target+1)
        dp[0]=0
        for t in range(1,target+1):
            for i in range(9):
                if t-cost[i]>=0:
                    dp[t]=max(dp[t],dp[t-cost[i]]+1)
        if dp[target]==float('-inf'):
            return '0'
        res=[]
        while target:
            for i in range(8,-1,-1): # iterate reversely to get the largest number
                if target-cost[i]>=0 and dp[target]==dp[target-cost[i]]+1: # generate the path/number
                    target-=cost[i]
                    res.append(str(i+1))
                    break

        return ''.join(res)
class Solution3:
    # tle
    def largestNumber(self, cost: List[int], target: int) -> str:
        def getMax(a:str,b:str):
            if len(a)>len(b):
                return a
            elif len(b)>len(a):
                return b
            return a if a>b else b

        dp={}
        for i in range(len(cost)):
            cst=cost[i]
            if cst not in dp:
                dp[cst]=str(i+1)
            else:
                dp[cst]=getMax(dp[cst],str(i+1))

        for cst in range(1,target+1):
            cur=dp.copy()
            for prev in dp:
                if cst-prev in cur:
                    if cst in cur:
                        cur[cst]=getMax(cur[cst],cur[prev]+cur[cst-prev])
                    else:
                        cur[cst]=cur[prev]+cur[cst-prev]
            dp=cur

        return dp[target] if target in dp else '0'
class Solution4:
    # tle
    def largestNumber(self, cost: List[int], target: int) -> str:
        def getMax(a:str,b:str):
            if len(a)>len(b):
                return a
            elif len(b)>len(a):
                return b
            return a if a>b else b

        dp={}
        for i in range(len(cost)):
            cst=cost[i]
            if cst not in dp:
                dp[cst]=str(i+1)
            else:
                dp[cst]=getMax(dp[cst],str(i+1))

        for cst in range(1,target+1):
            for prev in range(1,cst):
                if prev in dp and cst-prev in dp:
                    if cst in dp:
                        dp[cst]=getMax(dp[cst],dp[prev]+dp[cst-prev])
                    else:
                        dp[cst]=dp[prev]+dp[cst-prev]

        return dp[target] if target in dp else '0'


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual("7772", get_sol().largestNumber([4,3,2,5,6,7,2,5,5], 9))
    def test2(self):
        self.assertEqual("85", get_sol().largestNumber( [7,6,5,5,5,6,8,7,8], 12))
    def test3(self):
        self.assertEqual("0", get_sol().largestNumber([2,4,6,2,4,6,4,4,4], 5))
    def test4(self):
        self.assertEqual("0", get_sol().largestNumber([210,77,91,105,1208,511,3392,3029,1029], 4031))
    def test5(self):
        self.assertEqual("87432222222222222222222222222222222222222222222", get_sol().largestNumber([210,77,91,105,1908,3953,530,410,1237], 4447))
    def test6(self):
        self.assertEqual("5555443222", get_sol().largestNumber([1000,30,105,70,42,1000,1000,1000,1000], 503))
    # def test7(self):
    # def test8(self):
