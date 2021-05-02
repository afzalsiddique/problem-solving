import unittest
from collections import deque
from typing import List

from typing import List

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        minn=float('inf')
        for val in range(1,6+1):
            cnt,flag=0,True
            for i in range(n):
                if A[i]==val: continue
                if B[i]==val:
                    cnt+=1
                else:
                    flag=False
                    break
            if flag:minn=min(minn,cnt)
        for val in range(1,6+1):
            cnt,flag=0,True
            for i in range(n):
                if B[i]==val: continue
                if A[i]==val:
                    cnt+=1
                else:
                    flag=False
                    break
            if flag:minn=min(minn,cnt)
        return -1 if minn==float('inf') else minn

def get_sol_obj():
    return Solution()
class tester(unittest.TestCase):
    def test1(self):
        A = [2,1,2,4,2,2]
        B = [5,2,6,2,3,2]
        Output= 2
        self.assertEqual(Output,get_sol_obj().minDominoRotations(A, B))
    def test2(self):
        A = [3,5,1,2,3]
        B = [3,6,3,3,4]
        Output= -1
        self.assertEqual(Output,get_sol_obj().minDominoRotations(A, B))
