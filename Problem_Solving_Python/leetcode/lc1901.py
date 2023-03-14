import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/find-a-peak-element-ii/discuss/1276556/JavaPythonC%2B%2B-Clear-Explanation-with-Images-or-M*Log(N)-or-Very-Short-code
    def findPeakGrid(self, mat):
        startCol = 0
        endCol = len(mat[0])-1

        while True:
        # while startCol <= endCol:
            midCol = (endCol+startCol)//2
            maxRow = 0

            for row in range(len(mat)):
                if (mat[row][midCol] >= mat[maxRow][midCol]):
                    maxRow = row

            leftIsBig    =   midCol-1 >= startCol  and  mat[maxRow][midCol-1] > mat[maxRow][midCol]
            rightIsBig   =   midCol+1 <= endCol    and  mat[maxRow][midCol+1] > mat[maxRow][midCol]

            if (not leftIsBig) and (not rightIsBig):   # we have found the peak element
                return [maxRow, midCol]
            elif rightIsBig:             # if rightIsBig, then there is an element in 'right' that is bigger than all the elements in the 'midCol',
                startCol = midCol+1     # so 'midCol' cannot have 'peakPlane'
            else:                           # leftIsBig
                endCol = midCol-1

        # return []


class MyTestCase(unittest.TestCase):
    def test1(self):
        mat = [[1,4],[3,2]]
        Output= [0,1]
        self.assertEqual(Output, get_sol().findPeakGrid(mat))
    def test2(self):
        mat = [[10,20,15],[21,30,14],[7,16,32]]
        Output= [1,1]
        self.assertEqual(Output, get_sol().findPeakGrid(mat))
    def test3(self):
        self.assertEqual([3,7],get_sol().findPeakGrid([[1,2,3,4,5,6,7,8],[2,3,4,5,6,7,8,9],[3,4,5,6,7,8,9,10],[4,5,6,7,8,9,10,11]]))
    def test4(self):
        self.assertEqual([2,4],get_sol().findPeakGrid([[25,37,23,37,19],[45,19,2,43,26],[18,1,37,44,50]]))
    # def test5(self):
    # def test6(self):
    # def test7(self):
