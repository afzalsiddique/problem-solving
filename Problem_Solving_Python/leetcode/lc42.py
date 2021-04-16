# https://www.youtube.com/watch?v=m18Hntz4go8
import unittest
from heapq import *
from typing import List


# https://www.youtube.com/watch?v=cJayBq38VYw
class Solution:
    # constant space
    def trap(self, height: List[int]) -> int:
        n=len(height)
        l,r=0,n-1
        ans=0
        l_max,r_max=0,0
        while l<=r:
            if l_max<r_max:
                if l_max<height[l]:
                    l_max=height[l]
                else:
                    ans+=l_max-height[l]
                l+=1
            else:
                if r_max<height[r]:
                    r_max=height[r]
                else:
                    ans+=r_max-height[r]
                r-=1
        return ans

    ## priority queue
    def trap1(self, height: List[int]) -> int:
        n =len(height)
        if n==0 or n==1 or n==2:
            return 0
        pq = [(height[0],0),(height[-1],n-1)]
        vis = [False for _ in range(n)]
        vis[0],vis[n-1]=True,True
        heapify(pq)
        res,minn = 0,0
        while pq:
            curr_h, idx = heappop(pq)
            if curr_h>minn:
                minn=curr_h
            res+=minn-curr_h
            if idx+1<n and vis[idx+1]==False:
                heappush(pq,(height[idx+1],idx+1))
                vis[idx+1]=True
            if idx-1>=0 and vis[idx-1]==False:
                heappush(pq,(height[idx-1],idx-1))
                vis[idx-1]=True
        return res

    # linear space
    def trap3(self, height: List[int]) -> int:
        n=len(height)
        l_max, r_max = [0 for _ in range(n)], [0 for _ in range(n)] # prefix max and suffix max
        maxx = 0
        for i in range(n):
            maxx = max(maxx, height[i])
            l_max[i] = maxx
        maxx=0
        for i in reversed(range(n)):
            maxx = max(maxx, height[i])
            r_max[i] = maxx

        ans=0
        for i in range(n):
            minn = min(l_max[i],r_max[i])
            ans+= minn - height[i]
        return ans

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