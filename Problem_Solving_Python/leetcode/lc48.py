from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
# https://www.youtube.com/watch?v=Y72QeX0Efxw&t=207s

class Solution:
    # constant space
    def rotate(self, mat: List[List[int]]) -> None:
        m,n=len(mat),len(mat[0])
        for i in range(m):
            rightPtr=i
            downPtr=i
            while rightPtr<n and downPtr<m:
                mat[downPtr][i],mat[i][rightPtr]=mat[i][rightPtr],mat[downPtr][i]
                downPtr+=1
                rightPtr+=1
        for row in mat:
            row.reverse()
class Solution2:
    # constant space
    def rotate(self,matrix: List[List[int]]) -> None:
        def swap(nth):
            i,j=nth,nth
            while i<n:
                matrix[i][nth],matrix[nth][j]=matrix[nth][j],matrix[i][nth]
                i+=1
                j+=1
        def transpose():
            for nth in range(n):
                swap(nth)

        n = len(matrix)
        transpose()

        for row in matrix:
            row.reverse()


class MyTestCase(unittest.TestCase):
    def test_1(self):
        matrix=[[1,2,3],
                [4,5,6],
                [7,8,9]]
        e = [[7,4,1],[8,5,2],[9,6,3]]
        get_sol().rotate(matrix)
        self.assertEqual(e,matrix)
    def test_2(self):
        matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        e = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
        get_sol().rotate(matrix)
        self.assertEqual(e,matrix)
    def test_3(self):
        matrix = [[1]]
        e = [[1]]
        get_sol().rotate(matrix)
        self.assertEqual(e,matrix)
    def test_4(self):
        matrix = [[1,2],[3,4]]
        e = [[3,1],[4,2]]
        get_sol().rotate(matrix)
        self.assertEqual(e,matrix)
