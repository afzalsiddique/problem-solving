from heapq import *; import unittest; from typing import List;


def get_sol(): return Solution()
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        def getSum(colIndices:tuple[int]):
            res=0
            for i in range(m):
                res+=mat[i][colIndices[i]]
            return res
        def getNext(colIndices:tuple[int]):
            colIndices=list(colIndices)
            res=[]
            for i in range(m):
                if colIndices[i]+1<n:
                    tmp= colIndices[:i] + [colIndices[i] + 1] + colIndices[i + 1:]
                    res.append(tuple(tmp))
            return res

        m,n=len(mat),len(mat[0])
        vis=set()
        colIndices=tuple([0 for _ in range(m)])
        vis.add(colIndices)
        pq=[(getSum(colIndices),colIndices)]
        res=float('-inf')
        for i in range(k):
            if not pq: return res
            res,colIndices=heappop(pq)
            for nxtIdx in getNext(colIndices):
                if nxtIdx not in vis:
                    vis.add(nxtIdx)
                    heappush(pq,(getSum(nxtIdx),nxtIdx))
        return res


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(7, get_sol().kthSmallest(mat = [[1,3,11],[2,4,6]], k = 5))
    def test2(self):
        self.assertEqual(17, get_sol().kthSmallest(mat = [[1,3,11],[2,4,6]], k = 9))
    def test3(self):
        self.assertEqual(9, get_sol().kthSmallest(mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7))
    def test4(self):
        self.assertEqual(12, get_sol().kthSmallest(mat = [[1,1,10],[2,2,9]], k = 7))
    # def test5(self):
    # def test6(self):
    # def test7(self):

