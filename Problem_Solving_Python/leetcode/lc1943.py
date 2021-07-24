import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # line sweep
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        BIG = 100005
        BIG = 27 # delete this line. only for visualization
        acc = [[False, 0] for _ in range(BIG)]
        for start, end, color in segments:
            acc[start][1] += color
            acc[end][1] -= color
            acc[start][0] = True
            acc[end][0] = True

        last_segment_start = 0
        res = []
        for i in range(len(acc)):
            acc[i][1] += acc[i - 1][1]
            if acc[i][0]:
                if acc[i - 1][1] != 0:
                    res.append([last_segment_start, i, acc[i - 1][1]])
                last_segment_start = i
        return res
class Solution2:
    # similar to minimum platforms in gfg
    # https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        n=len(segments)
        ARRIVAL = True
        colors = {i:segments[i][2] for i in range(n)}
        arrivals=[(segments[i][0],i,ARRIVAL) for i in range(n)]
        leavings=[(segments[i][1],i,not ARRIVAL) for i in range(n)]
        arrivals.sort()
        leavings.sort()
        all = arrivals + leavings
        all.sort(key=lambda x:x[0])
        cnt=colors[all[0][1]]
        last=all[0][0]
        res=[]
        for i in range(1,len(all)):
            this=all[i][0]
            id = all[i][1]
            if all[i][2]==ARRIVAL:
                if last!=this and cnt!=0:
                    res.append([last,this,cnt])
                cnt+=colors[id]
            else:
                if last!=this and cnt!=0:
                    res.append([last,this,cnt])
                cnt-=colors[id]
            last=this
        return res

class Sample: # MINIMUM PLATFORM
    def solve(self, A):
        cnt,maxx=0,float('-inf')
        start = [(A[i][0],True) for i in range(len(A))]
        end = [(A[i][1],False) for i in range(len(A))]
        al = start+end
        al.sort()
        for time,arrival in al:
            if arrival:
                cnt+=1
                maxx=max(maxx,cnt)
            else:
                cnt-=1
        return maxx

class tester(unittest.TestCase):
    def test_1(self):
        segments = [[1,4,5],[4,7,7],[1,7,9]]
        Output= [[1,4,14],[4,7,16]]
        self.assertEqual(Output, get_sol().splitPainting(segments))
    def test_2(self):
        segments = [[1,7,9],[6,8,15],[8,10,7]]
        Output= [[1,6,9],[6,7,24],[7,8,15],[8,10,7]]
        self.assertEqual(Output, get_sol().splitPainting(segments))
    def test_3(self):
        segments = [[1,4,5],[1,4,7],[4,7,1],[4,7,11]]
        Output= [[1,4,12],[4,7,12]]
        self.assertEqual(Output, get_sol().splitPainting(segments))
    def test_4(self):
        segments = [[4,16,12],[9,10,15],[18,19,13],[3,13,20],[12,16,3],[2,10,10],[3,11,4],[13,16,6]]
        Output= [[2,3,10],[3,4,34],[4,9,46],[9,10,61],[10,11,36],[11,12,32],[12,13,35],[13,16,21],[18,19,13]]
        self.assertEqual(Output, get_sol().splitPainting(segments))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):