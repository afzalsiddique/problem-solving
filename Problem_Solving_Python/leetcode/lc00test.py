from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        pre = []
        curSum = sum(nums[i] for i in range(k-1))
        for i in range(k-1,len(nums)):
            curSum+=nums[i]
            pre.append(curSum)
            curSum-=nums[i-k+1]

        n=len(pre)
        left_max=[0]*n # index
        for i in range(1,n):
            if pre[i]>pre[left_max[i-1]]:
                left_max[i]=i
            else:
                left_max[i]=left_max[i-1]

        right_max=[n-1]*n # index
        for i in range(n-2,-1,-1):
            if pre[i]>=pre[right_max[i+1]]:
                right_max[i]=i
            else:
                right_max[i]=right_max[i+1]

        maxIdx=[None,None,None]
        maxSum=float('-inf')
        for i in range(n):
            left_fake_idx=i-k
            right_fake_idx=i+k
            if not left_fake_idx>=0 or not right_fake_idx<n: continue
            left=left_max[left_fake_idx]
            right=right_max[right_fake_idx]
            curIdx=[left,i,right]
            l,cur,r=pre[left],pre[i],pre[right]
            tmpSum=pre[left]+pre[i]+pre[right]
            if tmpSum>maxSum:
                maxIdx=[left,i,right]
                maxSum=tmpSum
            elif tmpSum==maxSum:
                maxIdx=min(maxIdx,curIdx)
        return maxIdx

class Correct:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        # calculate prefix sum
        pre=[] # prefix sum
        cur=0 # current_sum/running_sum
        left,right=0,0
        while right<k-1:
            cur+=nums[right]
            right+=1
        while right<n:
            cur+=nums[right]
            pre.append(cur)
            cur-=nums[left]
            left+=1
            right+=1

        left_max=[0]*len(pre) # index. first k are invalid
        right_max=[0]*len(pre) # index. last k are invalid
        idx=0
        for i in range(len(pre)-k):
            if pre[i]>pre[idx]:
                idx=i
            left_max[i+k]=idx

        idx=len(pre)-1
        for i in range(len(pre)-1,k-1,-1): # first k and last k values from the prefix sum are invalid
            if pre[i]>=pre[idx]:
                idx=i
            right_max[i-k]=idx
        # print(pre)
        # print(left_max)
        # print(right_max)

        maxx=float('-inf')
        for i in range(k,len(pre)-k):
            if pre[i]+pre[left_max[i]]+pre[right_max[i]]>maxx:
                res=[left_max[i],i,right_max[i]]
                maxx=pre[i]+pre[left_max[i]]+pre[right_max[i]]
        return res

class Tester(unittest.TestCase):
    def test01(self):
        a,b = [17,9,3,2,7] ,1
        self.assertEqual(Correct().maxSumOfThreeSubarrays(a,b), Solution().maxSumOfThreeSubarrays(a,b))
