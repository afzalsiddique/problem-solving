import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()

class Solution:
    # https://www.youtube.com/watch?v=uJ8BAQ8lASE
    def isPossible(self, nums)->bool:
        remaining = Counter(nums)
        attach_remain = defaultdict(int)
        for x in nums:
            if remaining[x]==0: continue
            if attach_remain[x]!=0: # if could be attached to existing subsequence
                remaining[x]-=1
                attach_remain[x]-=1
                attach_remain[x+1]+=1
            else: # if not possible to attach to existing subsequence then create a new subsequence of length 3
                for i in range(3):
                    if remaining[x+i]==0:
                        return False
                    remaining[x+i]-=1
                attach_remain[x+3]+=1
        return True
class Solution2:
    # https://www.youtube.com/watch?v=uJ8BAQ8lASE
    def isPossible(self, nums):
        remaining = Counter(nums)
        end = defaultdict(int)
        for i in nums:
            if not remaining[i]: continue
            elif end[i]>0:
                remaining[i]-=1
                end[i]-=1
                end[i+1]+=1
            elif remaining[i]>0 and remaining[i+1]>0 and remaining[i+2]>0:
                remaining[i]-=1
                remaining[i+1]-=1
                remaining[i+2]-=1
                end[i+3]+=1
            else:
                return False
        return True

class Solution3:
    # time O(nlogn) space O(n)
    # priority queue
    # https://leetcode.com/problems/split-array-into-consecutive-subsequences/discuss/106539/Python-Solution-using-PriorityQueue
    def isPossible(self, nums: List[int]) -> bool:
        di = defaultdict(list)
        for x in nums:
            if x-1 not in di:
                heappush(di[x],1)
            else:
                tmp = heappop(di[x-1])
                heappush(di[x],tmp+1)
                if not di[x-1]:
                    di.pop(x-1)
        for key in di:
            if di[key][0]<3: return False
        return True

class tester(unittest.TestCase):
    def test1(self):
        nums = [1,2,3,3,4,5]
        Output= True
        self.assertEqual(Output,Solution().isPossible(nums))
    def test2(self):
        nums = [1,2,3,3,4,4,5,5]
        Output= True
        self.assertEqual(Output,Solution().isPossible(nums))
    def test3(self):
        nums = [1,2,3,4,4,5]
        Output= False
        self.assertEqual(Output,Solution().isPossible(nums))
