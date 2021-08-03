import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        def manhattan(x1,y1,x2,y2): return abs(x1-x2)+abs(y1-y2)
        player_dist=manhattan(target[0],target[1],0,0)
        for x1,x2 in ghosts:
            if manhattan(x1,x2,target[0],target[1])<=player_dist: return False
        return True
class Solution2:
    # tle. bfs
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        def bfs(q:deque,target:List[int]):
            vis=set()
            cnt=0
            while q:
                for _ in range(len(q)):
                    i,j=q.popleft()
                    if [i,j]==target: return cnt
                    if (i,j) in vis: continue
                    vis.add((i,j))
                    for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]: q.append((i+di,j+dj))
                cnt+=1

        return bfs(deque([[0,0]]),target) < bfs(deque(ghosts),target)

class Tester(unittest.TestCase):
    def test1(self):
        ghosts,target = [[5,0],[-10,-2],[0,-5],[-2,-2],[-7,1]], [7,7]
        Output= False
        self.assertEqual(Output,get_sol().escapeGhosts(ghosts,target))
    def test2(self):
        ghosts,target = [[2,0]], [1,0]
        Output= False
        self.assertEqual(Output,get_sol().escapeGhosts(ghosts,target))
    def test3(self):
        ghosts,target = [[1,0]], [2,0]
        Output= False
        self.assertEqual(Output,get_sol().escapeGhosts(ghosts,target))
    def test4(self):
        ghosts,target = [[1,0],[0,3]], [0,1]
        Output= True
        self.assertEqual(Output,get_sol().escapeGhosts(ghosts,target))
    def test5(self):
        ghosts,target = [[-1,0],[0,1],[-1,0],[0,1],[-1,0]], [0,0]
        Output= True
        self.assertEqual(Output,get_sol().escapeGhosts(ghosts,target))
    def test6(self):
        ghosts,target = [[793,9579],[4375,8541],[7668,2976],[1405,-6226],[-6384,3429],[-8324,-1472],[4738,2717],[6182,2630],[-6738,1189],[-2851,-6597],[8377,6154],[6416,-4056],[-9358,-4503],[-5996,-4935],[-4087,8710],[-8537,-4851],[-4614,3900],[4628,850],[3892,8172],[6559,9750],[1704,-6017],[-1500,-4280],[5595,-8308],[1069,2097],[7171,-8754],[-2018,357],[-6349,-6607],[-9551,7222],[5196,-248],[5491,-1606],[1547,537],[-2657,-4177],[6582,-8872],[5436,-459],[6419,-3583],[-9798,8511],[-1802,6384],[-9717,7592],[839,9498],[2228,9980],[5455,-2751],[7210,2230],[-763,4687],[5444,-4496],[-2357,-8637],[7416,-9812],[-7962,-9934],[-8414,4825],[-7659,-5894],[8337,1484],[-5647,9054],[4581,-7605],[-3857,8343],[6834,9327],[-8837,-5064],[8680,958],[-3720,2124],[-535,1323],[-3436,-5330],[9440,-6890],[1872,-903],[-2410,598],[-154,9004],[-1512,2410],[9537,-7930],[-164,6859],[-1401,-4886],[6144,-9442],[6,-6827],[-8561,8014],[4617,7851],[-8756,-638],[4250,-6725],[1403,3367],[-1244,2536],[-8906,-9625],[-9950,1484],[7566,-9272],[7631,-665],[-1134,-6653],[-9273,-6891],[9110,2471],[-8844,-1683],[-3533,8801],[8585,-5125],[-5140,9914],[5212,-6899],[-6638,4092],[-7790,-901],[-4212,5948],[1526,2238],[-9513,7842],[1274,2462],[7528,116],[6648,-4132],[-6157,9177],[8119,1814],[-4279,-5573],[-8003,-9858],[-6671,3189]], [3649,6156]
        Output= False
        self.assertEqual(Output,get_sol().escapeGhosts(ghosts,target))
    # def test7(self):
