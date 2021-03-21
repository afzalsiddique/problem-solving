# https://www.youtube.com/watch?v=Y72QeX0Efxw&t=207s
from collections import deque, defaultdict
from heapq import *
import unittest
from typing import List
# constant space
class Solution:
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
        Solution().rotate(matrix)
        self.assertEqual(e,matrix)
    def test_2(self):
        matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        e = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
        Solution().rotate(matrix)
        self.assertEqual(e,matrix)
    def test_3(self):
        matrix = [[1]]
        e = [[1]]
        Solution().rotate(matrix)
        self.assertEqual(e,matrix)
    def test_4(self):
        matrix = [[1,2],[3,4]]
        e = [[3,1],[4,2]]
        Solution().rotate(matrix)
        self.assertEqual(e,matrix)
