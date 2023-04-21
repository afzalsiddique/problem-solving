import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List; from math import sqrt
def get_sol(): return Solution()
class Solution: # bfs
    # https://www.youtube.com/watch?v=R58Q0J52qzI
    def numBusesToDestination(self, routes: List[List[int]], src: int, target: int) -> int:
        if src==target: return 0
        stop_to_routes=defaultdict(set)
        for route_index, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(route_index)

        q=deque([[src,0]])
        # alternative
        # stop_to_routes['dummy'].update(stop_to_routes[src])
        # q=deque([['dummy',0]])

        seen_stops=set()
        seen_routes=set()
        while q:
            for _ in range(len(q)):
                from_stop,cnt=q.popleft()
                if from_stop==target: return cnt
                if from_stop in seen_stops: continue
                seen_stops.add(from_stop)
                for route_idx in stop_to_routes[from_stop]: # go to a different route and also explore the current route
                    if route_idx in seen_routes: continue
                    seen_routes.add(route_idx)
                    for to_stop in routes[route_idx]: # go to a stop located in a different route
                        q.append([to_stop,cnt+1])

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
    def test1(self):
        routes,source,target = [[1,2,7],[3,6,7]],  1,  6
        Output= 2
        self.assertEqual(Output, get_sol().numBusesToDestination(routes,source,target))
    def test2(self):
        routes,source,target = [[7,12],[4,5,15],[6],[15,19],[9,12,13]],  15,  12
        Output= -1
        self.assertEqual(Output, get_sol().numBusesToDestination(routes,source,target))
    def test3(self):
        routes,source,target = [[35,38],[10,37,38],[10,28,37]], 37, 28
        Output= 1
        self.assertEqual(Output, get_sol().numBusesToDestination(routes,source,target))
    def test4(self):
        routes,source,target = [[1,9,12,20,23,24,35,38],[10,21,24,31,32,34,37,38,43],[10,19,28,37],[8],[14,19],[11,17,23,31,41,43,44],[21,26,29,33],[5,11,33,41],[4,5,8,9,24,44]], 37, 28
        Output= 1
        self.assertEqual(Output, get_sol().numBusesToDestination(routes,source,target))
    def test5(self):
        routes,source,target = [[1,7],[3,5]], 5, 5
        Output= 0
        self.assertEqual(Output, get_sol().numBusesToDestination(routes,source,target))
    def test6(self):
        self.assertEqual(-1, get_sol().numBusesToDestination([[25,33],[3,5,13,22,23,29,37,45,49],[15,16,41,47],[5,11,17,23,33],[10,11,12,29,30,39,45],[2,5,23,24,33],[1,2,9,19,20,21,23,32,34,44],[7,18,23,24],[1,2,7,27,36,44],[7,14,33]], 7, 47))
    # def test7(self):
    # def test8(self):
