import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List




class NumMatrix:

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
