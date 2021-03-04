# https://www.youtube.com/watch?v=m18Hntz4go8
# https://www.youtube.com/watch?v=cJayBq38VYw
import unittest
from heapq import *
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n =len(height)
        if n==0 or n==1 or n==2:
            return 0
        pq = [(height[0],0),(height[-1],n-1)]
        vis = [False for _ in range(n)]
        vis[0],vis[n-1]=True,True
        heapify(pq)
        res,maxx = 0,0
        while pq:
            curr_h, idx = heappop(pq)
            if curr_h>maxx:
                maxx=curr_h
            else:
                res+=maxx-curr_h
            if idx+1<n and vis[idx+1]==False:
                heappush(pq,(height[idx+1],idx+1))
                vis[idx+1]=True
            if idx-1>=0 and vis[idx-1]==False:
                heappush(pq,(height[idx-1],idx-1))
                vis[idx-1]=True
        return res



class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])
        expected = 6
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.trap([4,2,0,3,2,5])
        expected = 9
        self.assertEqual(expected, actual)