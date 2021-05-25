import unittest
from collections import defaultdict

# check out leetcode 560
class Solution:
    def solve(self, nums, k):
        n = len(nums)
        di,ans=defaultdict(int),0
        pre=[0] * n
        pre[0] = nums[0]
        for i in range(1,n):
            pre[i] = pre[i-1]^nums[i]
        for i in range(n):
            if pre[i]==k:ans+=1
            y= pre[i]^k
            if y in di:
                ans+=di[y]
            di[pre[i]]+=1
        return ans

    # compare with count number sub arrays given sum
    # 6  +  8 = 14    14  -  8 = 6     14  -  6 = 8
    # 6 xor 8 = 13    13 xor 6 = 8     13 xor 8 = 6

