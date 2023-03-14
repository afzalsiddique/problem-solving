import unittest; from typing import List;


def get_sol(): return Solution()
class UnionFind:
    def __init__(self,n):
        self.n=n
        self.par=[i for i in range(n)]
        self.size=[1 for _ in range(n)]
    def __repr__(self): return str(self.par)
    def union(self,a,b):
        a=self.find(a)
        b=self.find(b)
        if a==b: return False
        if self.size[a]<self.size[b]:
            a,b=b,a
        self.par[b]=a
        self.size[a]+=self.size[b]
        return True
    def find(self,a):
        if a!=self.par[a]:
            self.par[a]=self.find(self.par[a])
        return self.par[a]
    def allConnected(self):
        return self.size[self.find(0)]==self.n
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(key=lambda x:-x[0]) # add type 3 edges first
        alice=UnionFind(n)
        bob=UnionFind(n)
        edgesAdded=0
        for t,u,v in edges:
            u-=1 # convert it to 0 based indexing
            v-=1
            if t==3:
                added=False
                added|=alice.union(u,v)
                added|=bob.union(u,v)
                edgesAdded += added
            elif t==2:
                edgesAdded += alice.union(u,v)
            else:
                edgesAdded += bob.union(u,v)

        if alice.allConnected() and bob.allConnected():
            return len(edges)-edgesAdded
        return -1

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(2, get_sol().maxNumEdgesToRemove(4, [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]))
    def test02(self):
        self.assertEqual(0, get_sol().maxNumEdgesToRemove(4, [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]))
    def test03(self):
        self.assertEqual(-1, get_sol().maxNumEdgesToRemove( 4, [[3,2,3],[1,1,2],[2,3,4]]))
    # def test04(self):
