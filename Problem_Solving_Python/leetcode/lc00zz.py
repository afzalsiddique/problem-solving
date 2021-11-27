import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], src: int, target: int) -> int:
        def construct(route_no, route):
            if len(route)==1: return
            for u,v in zip(route,route[1:]):
                g[u].append(v)
            g[route[-1]].append(route[0])

            for u in route:
                in_routes[u].add(route_no)

        def common_route(u,v):
            common = in_routes[u].intersection(in_routes[v])
            if common:
                return list(common)[0]
            return None

        def dijkstra(pq):
            dist=defaultdict(lambda :float('inf'))
            dist[src]=1
            vis=set()
            while pq:
                _,routes_taken,u=heappop(pq)
                if u in vis: continue
                vis.add(u)
                for v in g[u]:
                    new_routes_taken={x for x in routes_taken}
                    common=common_route(u,v)
                    if common: new_routes_taken.add(common)
                    if len(new_routes_taken)<dist[v]:
                        dist[v]=len(new_routes_taken)
                        heappush(pq,(len(new_routes_taken),new_routes_taken,v))
            res = dist[target]
            return -1 if res==float('inf') else res

        sett=set()
        for route in routes:
            sett.update(route)
        # n=len(sett)

        g=defaultdict(list)
        in_routes=defaultdict(set)
        for i,route in enumerate(routes):
            construct(i,route)

        res=float('inf')
        li = list(in_routes[src])
        for i in range(len(in_routes[src])):
            routes_taken_src= {li[i]}
            pq = [(len(routes_taken_src),routes_taken_src, src)]
            res=min(res,dijkstra(pq))

        # for route in routes:
        #     for x in route:
        #         print(x,':',dist[x])
        #     print()
        return -1 if res==float('inf') else res
class MyTestCase(unittest.TestCase):
    def test1(self):
        routes,source,target = [[1,2,7],[3,6,7]],  1,  6
        Output= 2
        self.assertEqual(Output, get_sol().numBusesToDestination(routes,source,target))
    def test2(self):
        routes,source,target = [[7,12],[4,5,15],[6],[15,19],[9,12,13]],  15,  12
        Output= -1
        self.assertEqual(Output, get_sol().numBusesToDestination(routes,source,target))
    def test3(self):
        routes,source,target = [[1,9,12,20,23,24,35,38],[10,21,24,31,32,34,37,38,43],[10,19,28,37],[8],[14,19],[11,17,23,31,41,43,44],[21,26,29,33],[5,11,33,41],[4,5,8,9,24,44]], 37, 28
        Output= 1
        self.assertEqual(Output, get_sol().numBusesToDestination(routes,source,target))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
