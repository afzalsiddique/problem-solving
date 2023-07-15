from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from Problem_Solving_Python.template.binary_tree import deserialize
mat=[[1,2,3],[4,5,6]]
def within(x:int,y:int)->bool:
    return 0<=x<len(mat) and 0<=y<len(mat[0])
def get_4d_moves(x:int, y:int)->List[tuple[int,int]]:
    return [(x+dx,y+dy) for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)] if within(x+dx,y+dy)]
def fromMatToTuple(mat:List[List[int]])->tuple[tuple[int]]:
    return tuple([tuple(row) for row in mat])
def fromTupleToMatrix(tup:tuple[tuple[int]])->List[List[int]]:
    return [list(row) for row in tup]
def nextGreaterElement(A):
    n=len(A)
    nxt=[-1]*n
    st=[]
    for i in range(n):
        while st and A[st[-1]]<A[i]:
            nxt[st.pop()]=A[i]
        st.append(i)
    return nxt
def nextGreaterOrEqualIndex(arr):
    # leetcode 975
    # this function finds next greater index. since it is sorted in ascending order, the next greater index
    # in this case will be the next smallest element of the greater elements in the smallest index.
    # also when sorted in descending order, it will find next smaller element of the smaller elements in the smallest index
    # check other solution for details
    n=len(arr)
    indices=sorted(range(n),key=lambda x:arr[x])
    n = len(indices)
    next_higher_or_equal = [-1]*n
    st = []
    for i in range(n):
        while st and indices[st[-1]] < indices[i]:
            next_higher_or_equal[indices[st.pop()]] = indices[i]
        st.append(i)
    return next_higher_or_equal
def nextGreaterOrEqualIndex2(arr): # index of next greater or equal element
    # leetcode 975
    # higher or equal value on the right with the smallest index. basically it is the immediate next element in a sorted array
    n=len(arr)
    next_higher_or_equal=[-1 for _ in range(n)]
    li = sorted([a, i] for i, a in enumerate(arr))
    st=[]
    for a,i in li:
        # since it is sorted based on value, we can just check whether it is on the right
        # then this will be the larger or equal value on the right side with the smallest index
        while st and st[-1]<i:
            next_higher_or_equal[st.pop()]=i
        st.append(i)
    return next_higher_or_equal
def nextSmallerElement(A):
    n=len(A)
    nxt=[-1]*n
    st=[]
    for i in range(n):
        while st and A[st[-1]]>A[i]:
            nxt[st.pop()]=A[i]
        st.append(i)
    return nxt
def nextLessOrEqualIndex(arr):
    n=len(arr)
    indices=sorted(range(n),key=lambda x:arr[x],reverse=True) # only one change -> reverse=True
    n = len(indices)
    next_lower_or_equal = [-1]*n
    st = []
    for i in range(n):
        while st and indices[st[-1]] < indices[i]: # no change here
            next_lower_or_equal[indices[st.pop()]] = indices[i]
        st.append(i)
    return next_lower_or_equal
def nextLessOrEqualIndex2(arr): # index of next smaller or equal element
    # lower or equal value on the right with the smallest index. basically it is the immediate previous element in a sorted array
    n=len(arr)
    next_lower_or_equal=[-1 for _ in range(n)]
    li = sorted([-a, i] for i, a in enumerate(arr))
    st=[]
    for a,i in li:
        while st and st[-1]<i:
            next_lower_or_equal[st.pop()]=i
        st.append(i)
    return next_lower_or_equal
