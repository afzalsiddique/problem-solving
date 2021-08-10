import unittest
from collections import deque, defaultdict

# NON-OVERLAPPING LEETCODE 1546
class Solution:
    def subarraySum(self, nums ,k):
        ## best example for thinking process ##
        # [5,5,10,-10,10], k= 10
        n = len(nums)
        ans=0
        mp = defaultdict(int)
        pre = [0 for _ in range(n)]# could be replaced by currentSum. no need for this array
        pre[0] = nums[0]
        for i in range(1,n):
            pre[i] = pre[i-1] + nums[i]
        for i in range(n):
            if pre[i] == k:
                ans+=1
            y = pre[i] - k
            if y in mp:
                ans+=mp[y]
            mp[pre[i]]+=1
        return ans
class Solution2:
    def subarraySum(self, nums ,k):
        n = len(nums)
        ans=0
        mp = defaultdict(int)
        mp[0]=1 # initializing like this also works
        pre = [0 for _ in range(n)]
        pre[0] = nums[0]
        for i in range(1,n):
            pre[i] = pre[i-1] + nums[i]
        for i in range(n):
            y = pre[i] - k
            if y in mp:
                ans+=mp[y]
            mp[pre[i]]+=1
        return ans

class tester(unittest.TestCase):
    def test1(self):
        # There are two types
        # a. sub array starting from the beginning where prefix sum = k
        # b. sub arrays in the middle
        # nums       = [5,5,10,-10,10]
        # prefix_sum = [5,10,20,10,20]
        # type a:
        #       1. [5+5]
        #       2. [5+5+10-10]
        # type b:
        #       1. [5+5+10] - [5+5] = [10]
        #             20        10     10
        #       2a. [5+5+10-10+10] - [5+5] = [10-10+10]
        #               20            10   =   10
        #       2b. [5+5+10-10+10] - [5+5+10-10] = [10]
        #               20              10          10
        # because of 2a and 2b set is not enough. Map is required.
        # total 5.
        self.assertEqual(5,Solution().subarraySum([5,5,10,-10,10],10))
        # compare with sub array with given xor
        # 6  +  8 = 14    14  -  8 = 6     14  -  6 = 8
        # 6 xor 8 = 13    13 xor 6 = 8     13 xor 8 = 6
    def test2(self):
        self.assertEqual(5,Solution().subarraySum([5,5,15,-15,0,0,25,5],30))
    def test3(self):
        self.assertEqual(9,Solution().subarraySum([3,4,7,2,-3,1,4,2,-13,0,7],7))
