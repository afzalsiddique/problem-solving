from itertools import accumulate; from math import floor,ceil,sqrt,log,log2; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt

# https://github.com/williamfiset/Algorithms/blob/master/src/main/java/com/williamfiset/algorithms/datastructures/sparsetable/examples/MinSparseTable.java
class MinSparseTable:
    def __init__(self,arr:List[int]):
        self.arr = arr
        self.buildTable(arr)
    def buildTable(self,arr:List[int]):
        n=len(arr)
        noOfRows = int(log(n) / log(2))
        self.dp = [[0]*n for _ in range(noOfRows+1)]

        for j in range(n):
            self.dp[0][j] = arr[j]

        for i in range(1,noOfRows+1):
            j=0
            while j + (1 << i) <= n:
                leftInterval = self.dp[i-1][j]
                rightInterval = self.dp[i-1][j + (1 << (i - 1))]
                self.dp[i][j] = min(leftInterval,rightInterval)
                j+=1

    def minQuery(self,l,r):
        length = r-l+1
        p = floor(log2(length))
        k = 1<<p
        return min(self.dp[p][l],self.dp[p][r-k+1])

def runSparseTable(s:str):
    inputs = convert_input(s)
    arr = inputs[1]
    sTable = MinSparseTable(arr)
    noOfQueries = inputs[2][0]
    res = []
    for i in range(3,noOfQueries+3):
        l,r = inputs[i]
        res.append(sTable.minQuery(l,r))
    return res

def convert_input(s:str)->List[List[int]]:
    s = s.split('\n')
    s = list(map(lambda x:x.split(" "), s))
    s = list(map(lambda li:[int(x) for x in li],s))
    return s

class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual([4,1,1,1],runSparseTable("3" # len of array
                                        "\n1 4 1" # array
                                        "\n4" # no of queries
                                        "\n1 1" # left and right range
                                        "\n2 2"
                                        "\n0 2"
                                        "\n0 1"))
