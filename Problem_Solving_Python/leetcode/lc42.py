from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import *; from a_linked_list import make_linked_list
def get_sol(): return Solution()
# https://www.youtube.com/watch?v=m18Hntz4go8
# https://www.youtube.com/watch?v=cJayBq38VYw
class Solution:
    # constant space
    def trap(self, A: List[int]) -> int:
        n=len(A)
        if n<=2: return 0
        pq=[]
        heappush(pq, (A[n - 1], n - 1, 'R'))
        heappush(pq, (A[0], 0, 'L'))
        res=0
        maxx=float('-inf')
        l,r=0,n-1
        while l<=r:
            if A[l]<A[r]:
                maxx=max(maxx,A[l])
                res+=max(0,maxx-A[l])
                l+=1
            else:
                maxx=max(maxx,A[r])
                res+=max(0,maxx-A[r])
                r-=1
        return res
class Solution5:
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
class Solution4:
    # priority queue and constant space
    def trap(self, A: List[int]) -> int:
        n=len(A)
        if n<=2: return 0
        pq=[]
        heappush(pq, (A[n - 1], n - 1, 'R'))
        heappush(pq, (A[0], 0, 'L'))
        res=0
        maxx=float('-inf')
        while pq:
            h,idx,side=heappop(pq)
            maxx=max(maxx,h)
            res+=max(0,maxx-h)
            if pq and (pq[0][1]==idx+1 or pq[0][1]==idx-1):
                break
            if side=='L':
                heappush(pq, (A[idx + 1], idx + 1, 'L'))
            else:
                heappush(pq, (A[idx - 1], idx - 1, 'R'))
        return res
class Solution2:
    # priority queue
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
            res+=maxx-curr_h
            if idx+1<n and vis[idx+1]==False:
                heappush(pq,(height[idx+1],idx+1))
                vis[idx+1]=True
            if idx-1>=0 and vis[idx-1]==False:
                heappush(pq,(height[idx-1],idx-1))
                vis[idx-1]=True
        return res
class Solution3:
    # linear space
    def trap(self, height: List[int]) -> int:
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
    def test01(self):
        self.assertEqual(6, get_sol().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    def test02(self):
        self.assertEqual(9, get_sol().trap([4,2,0,3,2,5]))
    def test03(self):
        self.assertEqual(0, get_sol().trap([0]))
