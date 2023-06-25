import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()
class Solution: # bfs
    # https://www.youtube.com/watch?v=R58Q0J52qzI
    def numBusesToDestination(self, routes: List[List[int]], src: int, target: int) -> int:
        if src==target: return 0
        stopToRoutes=defaultdict(set)
        for route_index, route in enumerate(routes):
            for stop in route:
                stopToRoutes[stop].add(route_index)

        q=deque([src])
        # alternative
        # stop_to_routes['dummy'].update(stop_to_routes[src])
        # q=deque([['dummy',0]])

        seenStops=set()
        seenRoutes=set()
        res=0
        while q:
            for _ in range(len(q)):
                frmStop=q.popleft()
                if frmStop==target: return res
                if frmStop in seenStops: continue
                seenStops.add(frmStop)
                for routeIdx in stopToRoutes[frmStop]: # go to a different route and also explore the current route
                    if routeIdx in seenRoutes: continue
                    seenRoutes.add(routeIdx)
                    for toStop in routes[routeIdx]: # go to a stop located in a different route
                        q.append(toStop)
            res+=1

        return -1
class Solution2:
    # tle
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source==target: return 0
        station_to_route=defaultdict(list)
        for r_i,r in enumerate(routes):
            for stop in routes[r_i]:
                station_to_route[stop].append(r_i)

        q=deque()
        for start_route_idx in station_to_route[source]:
            q.append([source,start_route_idx])

        res=1
        while q:
            for _ in range(len(q)):
                start_station,start_route_idx=q.popleft()
                for dest_station_same_route in routes[start_route_idx]:
                    if dest_station_same_route==target:
                        return res
                    if start_station==dest_station_same_route: continue
                    for dest_route_idx in station_to_route[dest_station_same_route]:
                        if dest_route_idx==start_route_idx:
                            continue
                        for dest_station_diff_route in routes[dest_route_idx]:
                            q.append([dest_station_diff_route,dest_route_idx])
            res+=1

        return -1
class Solution3:
    # wrong
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


        sett=set()
        for route in routes:
            sett.update(route)
        # n=len(sett)
        dist=defaultdict(lambda :float('inf'))
        dist[src]=1
        g=defaultdict(list)
        in_routes=defaultdict(set)
        for i,route in enumerate(routes):
            construct(i,route)

        routes_taken_src= {list(in_routes[src])[0]}
        pq = [(len(routes_taken_src),routes_taken_src, src)]
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
        for route in routes:
            for x in route:
                print(x,':',dist[x])
            print()
        return -1 if res==float('inf') else res


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(2, get_sol().numBusesToDestination( [[1,2,7],[3,6,7]],  1,  6))
    def test02(self):
        self.assertEqual(-1, get_sol().numBusesToDestination( [[7,12],[4,5,15],[6],[15,19],[9,12,13]],  15,  12))
    def test03(self):
        self.assertEqual(1, get_sol().numBusesToDestination( [[35,38],[10,37,38],[10,28,37]], 37, 28))
    def test04(self):
        self.assertEqual(1, get_sol().numBusesToDestination( [[1,9,12,20,23,24,35,38],[10,21,24,31,32,34,37,38,43],[10,19,28,37],[8],[14,19],[11,17,23,31,41,43,44],[21,26,29,33],[5,11,33,41],[4,5,8,9,24,44]], 37, 28))
    def test05(self):
        self.assertEqual(0, get_sol().numBusesToDestination( [[1,7],[3,5]], 5, 5))
    def test06(self):
        self.assertEqual(-1, get_sol().numBusesToDestination([[25,33],[3,5,13,22,23,29,37,45,49],[15,16,41,47],[5,11,17,23,33],[10,11,12,29,30,39,45],[2,5,23,24,33],[1,2,9,19,20,21,23,32,34,44],[7,18,23,24],[1,2,7,27,36,44],[7,14,33]], 7, 47))
    def test07(self):
        self.assertEqual(2, get_sol().numBusesToDestination([[1,21,24,29,35,55,57,64,65,69,72,77,93,104,107,117,128],[3,7,8,22,29,31,37,42,49,51,61,69,75,83,91,92,98,119,120],[9,25,45,67,103,105,122,128],[0,2,10,14,16,26,35,48,52,71,85,88,100,102,107,110,114,115,117,125,126],[1,14,25,33,36,38,41,47,48,53,57,76,85,86,87,93,96,97,102,105,106,114,122],[97],[7,22,30,39,47,66,70,86,87,101,104],[3,4,6,17,18,29,34,35,37,52,65,74,75,85,96,99,107,110,112,117],[40,45,70,72,83,87,101,121],[73,110],[5,11,17,31,41,44,51,63,87,90,91,94,97,98,109,114,118,126],[22,37,54,62,67,96,99,111,118],[5,20,21,34,35,42,55,56,82],[18,24,40,43,48,51,61,76,84,91,109,119,123],[5,11,14,18,23,36,42,43,50,51,53,61,70,75,76,81,85,88,92,94,95,103,105,128],[114],[11,17,19,21,23,28,46,47,59,67,72,73,74,75,79,86,87,89,101,102,105,111,126],[0,14,21,29,45,50,64,69,74,79,81,115,125,129],[4,9,22,33,39,45,55,66,69,70,78,84,89,97,98,107,110,113,114,120],[2,22,38,62,79,89,92,96,123],[22,40,55,65,105,107,119,126],[6,11,13,31,37,38,48,63,67,74,81,93,96,101,104,105,108,121,127],[3,19,40,42,69,79],[4,19,33,41,43,60,71,78,79,90,104,110,118,127],[16,26,27,36,37,49,68,91,92,108],[12,17,41,48,55,59,66,101,103]], 102, 66))
