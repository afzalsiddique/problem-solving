from bisect import *;
import unittest; from typing import List;
from sortedcontainers import SortedList


def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/closest-room/discuss/1185851/Python-Sorted-List-solution-explained
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        n=len(rooms)
        k=len(queries)
        R=sorted([[size,roomId] for roomId,size in rooms])[::-1]
        Q=sorted([[minSize,preferred,i] for i,(preferred,minSize) in enumerate(queries)])[::-1]
        p1,p2=0,0
        avail=SortedList()
        res=[-1]*k
        while p1<=n and p2<k:
            if p1<n and R[p1][0]>=Q[p2][0]:
                roomId=R[p1][1]
                avail.add(roomId)
                p1+=1
            else:
                if len(avail)!=0:
                    preferred, queryIdx = Q[p2][1], Q[p2][2]
                    i = avail.bisect(preferred)

                    cands=[]
                    if i > 0: cands.append(avail[i-1])
                    if i < len(avail): cands.append(avail[i])
                    res[queryIdx] = min(cands, key = lambda x: abs(x - preferred))
                p2+=1
        return res
class Solution2:
    # wrong
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        def roomSizeGreaterOrEqual(size):
            idx=bisect_left(roomSizes,size)
            if idx<len(roomSizes): # same size room
                return roomSizes[idx]
            idx=bisect_right(roomSizes,size) # greater size room
            if idx<len(roomSizes):
                return roomSizes[idx]
            return -1 # no room found
        def closestRoomId(li,preferred):
            if len(li)==0:
                return -1
            idx=bisect_left(li,preferred)
            if idx<len(li):
                return li[idx]

            minn=float('inf')
            ans=-1
            idx-=1
            if idx>=0:
                minn=abs(preferred-idx)
                ans=li[idx]

            idx=bisect_right(li,preferred)
            if idx<len(li):
                if abs(preferred-idx)<minn:
                    ans=li[idx]
            return ans

        N=max(max(rooms,key=lambda x:max(x[0],x[1])))
        roomSizes=set()
        li=[[] for _ in range(N+1)]
        for roomId,size in rooms:
            li[size].append(roomId)
            roomSizes.add(size)
        roomSizes=sorted(roomSizes)
        for i in range(N+1):
            li[i].sort()

        res=[]
        for preferred,minSize in queries:
            sizeIdx = roomSizeGreaterOrEqual(minSize)
            if sizeIdx==-1:
                res.append(-1)
                continue
            roomIdx= closestRoomId(li[sizeIdx],preferred)
            res.append(roomIdx)
        return res




class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual([3,-1,3],get_sol().closestRoom([[2,2],[1,2],[3,2]], [[3,1],[3,3],[5,2]]))
    def test2(self):
        self.assertEqual([2,1,3],get_sol().closestRoom([[1,4],[2,3],[3,5],[4,1],[5,2]], [[2,3],[2,4],[2,5]]))
    def test3(self):
        self.assertEqual([12,10,22,15,23,10,-1,5,23,15],get_sol().closestRoom([[23,22],[6,20],[15,6],[22,19],[2,10],[21,4],[10,18],[16,1],[12,7],[5,22]], [[12,5],[15,15],[21,6],[15,1],[23,4],[15,11],[1,24],[3,19],[25,8],[18,6]]))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
