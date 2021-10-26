import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        def dijkstra(g):
            final_dist = [float('inf') for _ in range(n)]
            final_dist[src]=0
            pq=[(0,src)]


            while pq:
                cur,u=heappop(pq)
                if cur>final_dist[u]: continue # optimization
                for v,cost in g[u]:
                    if cur+cost<final_dist[v]:
                        final_dist[v]=cur+cost
                        heappush(pq,(cur+cost,v))
            return final_dist

        n=len(patience)
        src=0
        g=defaultdict(list)
        for u,v in edges:
            g[u].append((v,1))
            g[v].append((u,1))
        final_dist = dijkstra(g)
        no_of_times = [] # no of time ith server has sent message
        for d,p in zip(final_dist,patience):
            if p==0:
                no_of_times.append(0)
            else:
                no_of_times.append(math.ceil(2*d/p))
        latest = [] # time when the ith server has sent last message
        for m,p in zip(no_of_times,patience):
            latest.append((m-1)*p)
        res =[]
        for l,d in zip(latest,final_dist):
            res.append(l+(2*d))
        # print('no_of_times:',no_of_times)
        # print('latest:',latest)
        # print('res:',res)
        return max(res)+1


class MyTestCase(unittest.TestCase):
    def test1(self):
        edges,patience = [[0,1],[1,2]],  [0,2,1]
        Output= 8
        self.assertEqual(Output, get_sol().networkBecomesIdle(edges,patience))
    def test2(self):
        edges,patience = [[0,1],[0,2],[1,2]], [0,10,10]
        Output= 3
        self.assertEqual(Output, get_sol().networkBecomesIdle(edges,patience))
    def test3(self):
        edges,patience = [[34,90],[82,5],[184,178],[92,32],[125,98],[149,134],[120,154],[37,129],[30,180],[161,2],[116,20],[42,12],[62,73],[96,162],[174,31],[124,101],[43,82],[87,59],[127,137],[103,7],[58,14],[119,133],[1,15],[84,113],[164,122],[128,104],[141,36],[81,166],[170,182],[89,30],[85,84],[109,1],[28,70],[83,102],[117,60],[31,169],[159,76],[146,67],[151,58],[23,34],[148,184],[179,19],[123,115],[70,21],[78,33],[99,26],[155,71],[104,100],[16,151],[72,147],[95,124],[13,138],[133,53],[60,116],[173,63],[29,56],[80,120],[17,43],[55,110],[6,119],[154,143],[51,172],[14,39],[112,38],[39,32],[35,132],[98,159],[160,107],[73,65],[183,27],[177,78],[136,46],[18,75],[27,91],[71,163],[100,77],[122,51],[178,45],[52,55],[59,160],[12,114],[38,42],[113,4],[163,167],[171,131],[167,183],[7,37],[102,54],[91,156],[40,92],[139,74],[142,145],[147,62],[0,128],[66,165],[111,175],[107,16],[22,80],[92,53],[94,86],[153,24],[74,3],[165,108],[176,130],[181,177],[67,95],[144,117],[15,135],[57,93],[145,8],[8,48],[26,127],[36,171],[126,40],[168,157],[108,121],[56,109],[65,88],[169,35],[130,181],[110,9],[2,22],[137,87],[152,118],[182,174],[53,32],[79,10],[114,47],[63,161],[0,94],[0,32],[76,150],[131,112],[129,105],[121,168],[118,111],[68,83],[69,61],[5,173],[172,149],[20,179],[162,57],[21,158],[166,11],[105,139],[93,44],[97,79],[106,23],[47,123],[46,49],[77,50],[157,153],[138,126],[0,69],[88,97],[24,68],[156,176],[92,39],[48,41],[158,170],[86,146],[61,142],[54,125],[19,148],[175,52],[44,85],[9,103],[135,144],[33,152],[90,66],[140,6],[101,28],[143,136],[75,96],[41,155],[53,39],[115,140],[150,13],[134,72],[180,164],[64,81],[45,106],[49,141],[50,89],[4,99],[11,25],[10,64],[25,17],[3,18],[132,29]], [0,5,4,6,8,6,10,3,11,1,9,1,9,13,9,9,12,3,6,7,2,5,1,4,7,4,18,10,7,9,16,1,24,1,5,15,5,8,11,2,27,4,10,1,3,4,3,8,1,10,12,21,3,2,17,1,1,1,5,3,4,29,11,2,4,2,9,9,12,9,2,10,9,7,5,7,9,3,10,2,7,4,8,3,12,4,16,6,4,22,6,13,20,1,2,8,1,2,5,16,29,16,5,1,27,2,5,22,1,6,4,5,7,5,15,5,4,5,4,6,8,5,8,24,23,17,7,8,3,1,7,5,2,17,4,5,11,9,16,1,12,13,26,1,7,4,18,1,7,12,19,12,1,10,3,3,14,8,15,19,22,1,4,22,14,1,4,1,11,11,13,2,2,1,1,7,8,2,2,1,15,3,4,19,1]
        Output= 123
        self.assertEqual(Output, get_sol().networkBecomesIdle(edges,patience))
    def test4(self):
        edges,patience = [[0,1],[1,2],[2,3]],  [0,100,100,4]
        Output= 11
        self.assertEqual(Output, get_sol().networkBecomesIdle(edges,patience))
    # def test5(self):
    # def test6(self):
