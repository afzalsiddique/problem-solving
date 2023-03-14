import unittest; from typing import List; import functools


def get_sol(): return Solution()
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @functools.lru_cache(None)
        def func(i, left):
            if i==len(nums):
                if left==0:
                    return 1
                return 0
            return func(i + 1, left + nums[i]) + func(i + 1, left - nums[i])

        return func(0,target)
class Solution4:
    # https://www.youtube.com/watch?v=MqYLmIzl8sQ
    # https://www.youtube.com/watch?v=hqGa65Rp5LQ&t=312s
    # https://www.youtube.com/watch?v=QihB4bI6BJw
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        summ = sum(nums)
        if summ < S or (summ + S) % 2 == 1:
            return 0
        target = (summ + S) // 2
        return self.sumSubset(nums, target)
    def sumSubset(self, nums, target):
        n = len(nums)
        nums = [0] + nums
        dp = [[0]*(target+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1
        for i in range(1,n+1):
            for j in range(1,target+1): # j is the capacity of the bag
                include,exclude=0,0
                if j<nums[i]: # if the capacity of the bag is less than nums[i]
                    exclude=dp[i-1][j] # only exclude
                elif nums[i] == 0: # if we encounter 0 skip it
                    exclude=dp[i-1][j]
                else:
                    exclude = dp[i-1][j]
                    include = dp[i-1][j-nums[i]]
                dp[i][j]=include+exclude
        zeros = sum(x==0 for x in nums) # count no of zeros
        zeros-=1 # because we added one extra zero at the beginning
        return int(2**zeros) * dp[-1][-1] # see below for explanation

# For those who has problem with test case  [0,0,0,0,0,0,0,0,1], target = 1.
# The solution doesn't consider presence of "0"s in the array. Why the output is different ?
# Because, if we have "0", then, it can have +0 and -0 and still will not effect the sum of a set. For example: Target value is = 2
# 1) {0,2} = {+0,2}, {-0,2}.  Ans: 2
# But if we increase number of 0s,
# 2) {0,0,2} = {+0,+0,2}, {+0,-0,2}, {-0,+0,2},{-0,-0,2} . Ans: 4
#
# So, if you observe, your answer increase by (2^number of 0s) i.e. pow(2,number of zeros).
# So, make a small change as follows:
# 1) on count of subsetsum function,
# if(nums[i-1] > j )    => change to:  if (nums[i-1] > j || nums[i-1] == 0)
#       dp[i][j] = dp[i-1][j];
#  //make no change and put the previous value as it is in the next subproblem. (I.e. 2, in example above)
# And then at the end, you answer will be
# return (int)Math.pow(2, number of 0s) * dp[nums.length][target] ;
#
# Also, other cases we need to handle is:
# if (S > sum || (sum + S) % 2 != 0){ //S is target
#             return 0;

class Solution2:
    # i don't know why this code below works :(
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        summ = sum(nums)
        if summ < S or (summ + S) % 2 == 1:
            return 0
        target = (sum(nums)+S) // 2
        return self.sumSubset(nums, target)
    def sumSubset(self, nums, target):
        n = len(nums)
        nums = ['#'] + nums
        dp = [[0]*(target+1) for _ in range(n+1)]
        # for i in range(n+1): ## changes here
        #     dp[i][0] = 1
        dp[0][0] = 1 ## changes here
        for i in range(1,n+1):
            for j in range(0,target+1):
                if j>=nums[i]: ## changes here
                    dp[i][j]=dp[i-1][j]+dp[i-1][j-nums[i]]
                else:
                    dp[i][j]=dp[i-1][j]
        zeros = 0
        for num in nums:
            if num==0:zeros+=1
        # return int(2**zeros) * dp[-1][-1] ## changes here
        return dp[-1][-1] ## changes here


class Tester(unittest.TestCase):
    # def test01(self):
    #     self.assertEqual(2,get_sol().sumSubset([1,2,1],3))
    def test02(self):
        self.assertEqual(0,get_sol().findTargetSumWays([1],2))
    def test03(self):
        self.assertEqual(256,get_sol().findTargetSumWays([0,0,0,0,0,0,0,0,1],1))
    def test04(self):
        self.assertEqual(2,get_sol().findTargetSumWays([1,0],1))
    def test05(self):
        self.assertEqual(792,get_sol().findTargetSumWays([1,1,1,1,1,1,1,1,1,1,1,1],2))
    def test06(self):
        self.assertEqual(5,get_sol().findTargetSumWays([1,1,1,1,1], 3))
    def test07(self):
        self.assertEqual(0,get_sol().findTargetSumWays([1,1,1,1], 3))
    def test08(self):
        self.assertEqual(1,get_sol().findTargetSumWays([1,1,1], 3))
    def test09(self):
        self.assertEqual(5564,get_sol().findTargetSumWays([50,37,6,20,35,41,45,3,20,36,49,1,20,10,43,4,44,15,44,34], 25))
    def test10(self):
        self.assertEqual(7219,get_sol().findTargetSumWays([42,36,4,15,17,15,31,1,11,2,12,28,22,9,2,31,48,18,48,5], 15))
