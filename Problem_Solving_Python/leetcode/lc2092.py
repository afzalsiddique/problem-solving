from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import *
def get_sol(): return Solution()
class UnionFind:
    # there should one component with size>1 and every other components will be with exactly size=1
    # for every timestamp perform union find operation
    # reset a person if he does not the secret after a particular timestamp
    # reset operation is -> self.par[a]=a
    def __init__(self,n):
        self.n=n
        self.par=[i for i in range(n)]
        self.size=[1 for _ in range(n)]
    def __repr__(self): return str(self.par)
    def union(self,a,b):
        a=self.find(a)
        b=self.find(b)
        if a!=b:
            if self.size[a]<self.size[b]:
                a,b=b,a
            self.par[b]=a
            self.size[a]+=self.size[b]
    def find(self,a):
        if a!=self.par[a]:
            self.par[a]=self.find(self.par[a])
        return self.par[a]
    def reset(self,a):
        self.par[a]=a
    def sameGroup(self,a,b):
        return self.find(a)==self.find(b)
    def secretGroup(self):
        return [i for i in range(self.n) if self.sameGroup(0,i)]
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        di=defaultdict(list) # di[time]=[[person,person]] # this could be removed for improved space complexity
        for x,y,time in meetings:
            di[time].append([x,y])

        uf=UnionFind(n)
        uf.union(0,firstPerson)
        for time in sorted(di):
            tmpMeetings=di[time]
            for x,y in tmpMeetings:
                uf.union(x,y)
            for x,y in tmpMeetings:
                if not uf.sameGroup(0,x): # if x and y does not know the secret then reset
                    uf.reset(x)
                    uf.reset(y)
        return uf.secretGroup()
class UnionFind2:
    # tle
    def __init__(self,n):
        self.n=n
        self.par=[i for i in range(n)]
        self.size=[1 for _ in range(n)]
    def __repr__(self): return str(self.par)
    def union(self,a,b):
        a=self.find(a)
        b=self.find(b)
        if a!=b:
            if self.size[a]<self.size[b]:
                a,b=b,a
            self.par[b]=a
            self.size[a]+=self.size[b]
    def find(self,a):
        if a!=self.par[a]:
            self.par[a]=self.find(self.par[a])
        return self.par[a]
    def allComponents(self):
        di=defaultdict(set)
        for i in range(self.n):
            di[self.find(i)].add(i)
        return [v for v in di.values()]
    def sameGroup(self,a,b):
        return self.find(a)==self.find(b)
    def secretGroup(self):
        return [i for i in range(self.n) if self.sameGroup(0,i)]
class Solution:
    # tle
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        def getComponents(E:List[List[int]]):
            uf=UnionFind2(n)
            for u,v in E:
                uf.union(u,v)
            return uf.allComponents()

        di=defaultdict(list)
        for x,y,time in meetings:
            di[time].append([x,y])

        uf=UnionFind2(n)
        uf.union(0,firstPerson)
        for time in sorted(di):
            comps = getComponents(di[time])
            for comp in comps:
                if any(uf.sameGroup(x,0) for x in comp):
                    for x in comp:
                        uf.union(x,0)
        return uf.secretGroup()
class Solution2:
    # wrong. When a new person learns the secret sorting should be updated
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        knowsSecret={0,firstPerson}
        meetings.sort(reverse=True,key=lambda x:(-x[2],x[0] in knowsSecret or x[1] in knowsSecret))
        for x,y,time in meetings:
            if x in knowsSecret or y in knowsSecret:
                knowsSecret.update([x,y])
        return list(knowsSecret)

class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual([0,1,2,3,5], get_sol().findAllPeople(6, [[1,2,5],[2,3,8],[1,5,10]],  1))
    def test02(self):
        self.assertEqual([0,1,3], get_sol().findAllPeople(4, [[3,1,3],[1,2,2],[0,3,3]], 3))
    def test03(self):
        self.assertEqual([0,1,2,3,4], get_sol().findAllPeople( 5, [[3,4,2],[1,2,1],[2,3,1]], 1))
    def test04(self):
        self.assertEqual([0,1,3,4], get_sol().findAllPeople(5, [[1,4,3],[0,4,3]], 3))
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
