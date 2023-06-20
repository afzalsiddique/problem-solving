import unittest; from typing import List;


def get_sol(): return Solution()
class UnionFind:
    def __init__(self,n):
        self.par=[i for i in range(n)]
        self.size=[1]*n
    def __repr__(self): return str(self.par)
    def find(self,a:int):
        if self.par[a]!=a:
            self.par[a]=self.find(self.par[a])
        return self.par[a]
    def union(self,a:int,b:int):
        a,b = self.find(a),self.find(b)
        if a!=b:
            if self.size[a]<self.size[b]:
                a,b=b,a
            self.par[b]=a
            self.size[a]+=self.size[b]
    def noOfBricksConnectedToTop(self): # there is a dummy brick positioned at 0
        return self.size[self.find(0)]-1 # subtract the dummy brick

class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        def oneDim(i,j): # 2d array index to 1d array index
            return i*n+j+1 # 1 indexed. because there is a dummy root brick at 0
        def unionAround(i, j, uf:UnionFind):
            for di, dj in [[-1,0],[1,0],[0,1],[0,-1]]:
                newI, newJ = i + di, j + dj
                if not 0 <= newI < m or not 0 <= newJ < n: continue
                if grid[newI][newJ] != 1: continue
                uf.union(oneDim(i, j), oneDim(newI, newJ))

            if i == 0: uf.union(0, oneDim(i, j))

        m,n=len(grid),len(grid[0])
        uf=UnionFind(m * n + 1) # '+1' because dummy root brick at position 0
        for x,y in hits:
            if grid[x][y]==1:
                grid[x][y]=2
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    unionAround(i,j,uf)

        res=[-1]*len(hits)
        cnt=uf.noOfBricksConnectedToTop()
        for i in range(len(hits)-1,-1,-1):
            x,y=hits[i]
            if grid[x][y]==0:
                res[i]=0
            else:
                grid[x][y]=1 # back to given array
                unionAround(x,y,uf)
                newCnt=uf.noOfBricksConnectedToTop()
                res[i]=max(0,newCnt-cnt-1) # '-1' because the brick which was hit is not counted
                cnt=newCnt
        return res
class Solution2:
    # tle
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        def canReachTop(i,j,vis):
            if not 0<=i<m or not 0<=j<n: return False
            if grid[i][j]==0: return False
            if (i,j) in vis: return False
            vis.add((i, j))
            if i==0: return True
            res=False
            for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                res=res or canReachTop(i+di,j+dj,vis)
            return res
        def remove_falling_bricks(vis:set[int]):
            for i,j in vis:
                grid[i][j]=0


        res=[]
        m,n=len(grid),len(grid[0])
        for x,y in hits:
            ans=0
            if grid[x][y]!=0:
                grid[x][y]=0
                for di,dj in [(0,1),(1,0),(-1,0),(0,-1)]:
                    vis=set()
                    if not canReachTop(x+di,y+dj,vis):
                        ans+=len(vis)
                        remove_falling_bricks(vis)
            res.append(ans)
        return res


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual([2], get_sol().hitBricks(grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]))
    def test2(self):
        self.assertEqual([0,0], get_sol().hitBricks(grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]))
    def test3(self):
        self.assertEqual([1,0,1,0,0], get_sol().hitBricks([[1],[1],[1],[1],[1]], [[3,0],[4,0],[1,0],[2,0],[0,0]]))
    def test4(self):
        self.assertEqual([0,3,0], get_sol().hitBricks([[1,0,1],[1,1,1]], [[0,0],[0,2],[1,1]]))
    def test5(self):
        self.assertEqual([0,0], get_sol().hitBricks([[1,0,1],[0,0,1]], [[1,0],[0,0]]))
    def test6(self):
        self.assertEqual([0,0,1,0], get_sol().hitBricks([[1,1,1],[0,1,0],[0,0,0]], [[0,2],[2,0],[0,1],[1,2]]))
