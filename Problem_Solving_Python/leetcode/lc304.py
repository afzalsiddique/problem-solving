import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(m): return NumMatrix(m)
class NumMatrix:
    # padded with zeros around the borders
    def __init__(self, mat: List[List[int]]):
        self.mat=mat
        m,n= len(mat), len(mat[0])
        for row in mat:
            row.append(0)
        mat.append([0] * (n + 1))
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                mat[i][j]+=mat[i+1][j]+mat[i][j+1]-mat[i+1][j+1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        mat=self.mat
        return mat[row1][col1]-mat[row2+1][col1]-mat[row1][col2+1]+mat[row2+1][col2+1]

class NumMatrix3:
    # no padding with zeros around the borders
    def __init__(self, mat: List[List[int]]):
        self.mat=mat
        m,n= len(mat), len(mat[0])
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                mat[i][j]+=mat[i+1][j] if i+1<m else 0
                mat[i][j]+=mat[i][j+1] if j+1<n else 0
                mat[i][j]-=mat[i+1][j+1] if i+1<m and j+1<n else 0
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        mat=self.mat
        m,n= len(mat), len(mat[0])
        res=mat[row1][col1]
        res-=mat[row2+1][col1] if row2+1<m else 0
        res-=mat[row1][col2+1] if col2+1<n else 0
        res+=mat[row2+1][col2+1] if row2+1<m and col2+1<n else 0
        return res
class NumMatrix2:
    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        self.row,self.col=len(matrix),len(matrix[0])
        self.pre = [[0]*self.col for _ in range(self.row)]
        self.__initialize_prefix_table()
        for p in self.pre:
            print(p)
    def __initialize_prefix_table(self):
        pre=self.pre
        col,row=self.col,self.row
        matrix=self.matrix
        for i in range(row):
            temp=0
            for j in range(col):
                temp+=matrix[i][j]
                pre[i][j]=temp

    def __getranges(self,row1,col1,row2,col2):
        ranges=[]
        for i in range(row1,row2+1): # right bound is including
            ranges.append((i,col1,col2)) # row_no, left,right
        print('get ranges:')
        print(ranges)
        return ranges

    def __get_sum(self,row_no,left,right):
        pre=self.pre
        if left!=0:
            return pre[row_no][right]-pre[row_no][left-1]
        return pre[row_no][right]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        summ=0
        ranges=self.__getranges(row1,col1,row2,col2)
        for r in ranges:
            summ+=self.__get_sum(r[0],r[1],r[2])
        return summ
class tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='NumMatrix':
                obj = NumMatrix(input[0])
                outputs.append(None)
            elif cmd=='sumRegion':
                outputs.append(obj.sumRegion(input[0],input[1],input[2],input[3]))
        return outputs
    def test_1(self):
        commands = ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
        inputs=[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
        out_exptected = [None, 8, 11, 12]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(out_exptected,outputs)
    def test_2(self):
        commands = ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
        inputs= [[[[1],[-7]]],[0,0,0,0],[1,0,1,0],[0,0,1,0]]
        out_exptected = [None, 1, -7, -6]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(out_exptected,outputs)
    def test_3(self):
        commands = ["NumMatrix", "sumRegion"]
        inputs= [    [ [[5,2],[3,6]]  ],[1,1,1,1]]
        out_exptected = [None, 6]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(out_exptected,outputs)
