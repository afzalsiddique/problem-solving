import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        EMPTY,BLOCKED = ' ','#'
        LEFT,RIGHT,UP,DOWN = [(0,-1),(0,1),(-1,0),(1,0)]
        def place(x,y,dir):
            di,dj = dir[0]*(-1),dir[1]*(-1) # opposite dir
            i,j=x+di,y+dj
            if 0<=i<m and 0<=j<n and board[i][j]!=BLOCKED: return False # empty space or other letters in the opposite direction

            di,dj = dir
            i1,j1 = x,y
            word_i=0
            while 0<=i1<m and 0<=j1<n:
                if board[i1][j1]==BLOCKED: break
                if word_i==len(word): return False # more than enough empty space
                if board[i1][j1]!=EMPTY and board[i1][j1]!=word[word_i]: return False
                word_i+=1
                i1,j1 = i1+di,j1+dj
            if abs(j1-y)!=len(word) and abs(i1-x)!=len(word): return False

            i2,j2 = x,y
            for word_i in range(len(word)):
                word_i+=1
                i2,j2 = i2+di,j2+dj
            return True

        m,n=len(board),len(board[0])
        for i in range(m):
            for j in range(n):
                if place(i,j,LEFT): return True
                if place(i,j,RIGHT): return True
                if place(i,j,UP): return True
                if place(i,j,DOWN): return True
        return False


class MyTestCase(unittest.TestCase):
    def test1(self):
        board,word = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]],  "abc"
        Output= True
        self.assertEqual(Output, get_sol().placeWordInCrossword(board,word))
    def test2(self):
        board,word = [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]],  "ac"
        Output= False
        self.assertEqual(Output, get_sol().placeWordInCrossword(board,word))
    def test3(self):
        board,word = [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]],  "ca"
        Output= True
        self.assertEqual(Output, get_sol().placeWordInCrossword(board,word))
    def test4(self):
        board,word = [["z"," "],["z"," "]],  "a"
        Output= False
        self.assertEqual(Output, get_sol().placeWordInCrossword(board,word))
    # def test5(self):
    # def test6(self):
