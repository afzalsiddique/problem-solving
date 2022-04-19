from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, lru_cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
# def get_sol(): return solution()
def solution(A):
    m,n=len(A),len(A[0])
    row_first_max=[float('-inf')]*m
    row_first_max_index=[(-1,-1)]*m
    row_second_max=[float('-inf')]*m
    row_second_max_index=[(-1,-1)]*m

    for i in range(m):
        for j in range(n):
            if A[i][j]>=row_first_max[i]:
                row_second_max[i]=row_first_max[i]
                row_second_max_index[i]=row_first_max_index[i]
                row_first_max[i]=A[i][j]
                row_first_max_index[i]=(i,j)


    col_first_max=[float('-inf')]*n
    col_first_max_index=[(-1,-1)]*n
    col_second_max=[float('-inf')]*n
    col_second_max_index=[(-1,-1)]*n

    for j in range(n):
        for i in range(m):
            if A[i][j]>=col_first_max[j]:
                col_second_max[j]=col_first_max[j]
                col_second_max_index[j]=col_first_max_index[j]
                col_first_max[j]=A[i][j]
                col_first_max_index[j]=(i,j)

    # print(col_first_max)
    # print(col_first_max_index)

    res=0
    for i in range(m):
        row_selected_one,col_selected_one=row_first_max_index[i]
        for j in range(n):
            row_selected_two,col_selected_two=col_first_max_index[j]
            if row_selected_two!=row_selected_one and col_selected_two!=col_selected_one:
                res=max(res,row_first_max[i]+col_first_max[j])
            row_selected_two,col_selected_two=col_second_max_index[j]
            if row_selected_two!=row_selected_one and col_selected_two!=col_selected_one:
                res=max(res,row_first_max[i]+col_second_max[j])
    return res


# class Tester(unittest.TestCase):
#     def test01(self): # 4+2
#         self.assertEqual(6,solution([
#             [1,4],
#             [2,3]
#         ]))
#     def test02(self): # 15+8
#         self.assertEqual(23,solution([
#             [15,1,5],
#             [16,3,8],
#             [2,6,4]
#         ]))
#     def test03(self): # 12+12
#         self.assertEqual(24,solution([
#             [12,12],
#             [12,12],
#             [0,7]
#         ]))
#     def test04(self): # 14+8
#         self.assertEqual(22,solution([
#             [1,2,14],
#             [8,3,15]
#         ]))
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
    # def test10(self):
