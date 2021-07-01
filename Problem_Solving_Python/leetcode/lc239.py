from heapq import *
import unittest
from collections import *
from typing import List



class Solution:
    # deque
    # https://www.youtube.com/watch?v=ShbRCjvB_yQ
    def maxSlidingWindow(self, nums, k):
        if not nums: return []
        res = []
        dq = deque()  # store index
        for i in range(len(nums)):
            if dq and dq[0]<=i-k:  # out of the window
                dq.popleft()
            while dq and nums[dq[-1]]<=nums[i]:  # remove impossible candidate
                dq.pop()
            dq.append(i)
            if i>=k-1:
                res.append(nums[dq[0]])
        return res


class Solution2:
    # heap
    # https://www.youtube.com/watch?v=LiSdD3ljCIE
    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        pq, n= [], len(nums)
        res = []
        for i in range(k-1):
            heappush(pq, (-nums[i],i)) # pq is (-val,idx)
        for i in range(n-k+1):
            heappush(pq, (-nums[i+k-1], i+k-1))
            val, idx = pq[0]
            res.append(val*(-1)) # append the max val
            while pq and pq[0][1] <= i: # remove the nodes which are dated
                heappop(pq)
        return res

class Solution3:
    # deque
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        for i in range(k-1):
            while q and q[-1][1]<nums[i]:
                q.pop()
            q.append((i,nums[i])) # idx, value

        res=[]
        for i in range(k-1,len(nums)):
            while q and q[0][0]<=i-k:
                q.popleft()
            while q and q[-1][1]<nums[i]:
                q.pop()
            q.append((i,nums[i])) # idx, value
            res.append(q[0][1])
        return res

class MyTestCase(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        actual = sol.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3)
        expected = [3,3,5,5,6,7]
        self.assertEqual(expected, actual)
    def test_2(self):
        sol = Solution()
        actual = sol.maxSlidingWindow(nums = [1], k = 1)
        expected = [1]
        self.assertEqual(expected, actual)
    def test_3(self):
        sol = Solution()
        actual = sol.maxSlidingWindow(nums = [1,-1], k = 1)
        expected = [1,-1]
        self.assertEqual(expected, actual)
    def test_4(self):
        sol = Solution()
        actual = sol.maxSlidingWindow(nums = [9,11], k = 2)
        expected = [11]
        self.assertEqual(expected, actual)
    def test_5(self):
        sol = Solution()
        actual = sol.maxSlidingWindow(nums = [4,-2], k = 2)
        expected = [4]
        self.assertEqual(expected, actual)
    def test_6(self):
        sol = Solution()
        actual = sol.maxSlidingWindow([9,10,9,-7,-4,-8,2,-6],5)
        expected = [10,10,9,2]
        self.assertEqual(expected, actual)

