import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/valid-tic-tac-toe-state/discuss/117580/Straightforward-Java-solution-with-explaination
    def validTicTacToe(self, board: List[str]) -> bool:
        turns = 0 # total X - total O
        row=[0]*3
        col=[0]*3
        diag1=0
        diag2=0
        x_wins=False
        o_wins=False
        for i in range(3):
            for j in range(3):
                if board[i][j]=='X':
                    turns+=1
                    row[i]+=1
                    col[j]+=1
                    if i==j: diag1+=1
                    if i+j==2: diag2+=1
                elif board[i][j]=='O':
                    turns-=1
                    row[i]-=1
                    col[j]-=1
                    if i==j: diag1-=1
                    if i+j==2: diag2-=1
        if row[0]==3 or row[1]==3 or row[2]==3 or col[0]==3 or col[1]==3 or col[2]==3 or diag1==3 or diag2==3:
            x_wins=True
        if row[0]==-3 or row[1]==-3 or row[2]==-3 or col[0]==-3 or col[1]==-3 or col[2]==-3 or diag1==-3 or diag2==-3:
            o_wins=True
        if turns!=0 and turns!=1: # no_of_x can be one greater than no_of_o or equal to no_of_o
            return False
        if x_wins and o_wins:
            return False
        if x_wins and turns!=1: # no_of_x should be no_of_o+1
            return False
        if o_wins and turns!=0: # no_of_o should be equal to no_of_x
            return False
        return True
class Solution2:
    X=1
    O=-1
    def check_if_wins(self,board:List[List[int]]):
        x=self.X
        o=self.O
        r0 = True if sum([1 for j in range(3) if board[0][j]==x])==3 else False
        r1 = True if sum([1 for j in range(3) if board[1][j]==x])==3 else False
        r2 = True if sum([1 for j in range(3) if board[2][j]==x])==3 else False
        c0 = True if sum([1 for i in range(3) if board[i][0]==x])==3 else False
        c1 = True if sum([1 for i in range(3) if board[i][1]==x])==3 else False
        c2 = True if sum([1 for i in range(3) if board[i][2]==x])==3 else False
        diag1 = True if sum([1 for i in range(3) for j in range(3) if board[i][j]==x and i==j])==3 else False
        diag2 = True if sum([1 for i in range(3) for j in range(3) if board[i][j]==x and i+j==2])==3 else False

        if r0 or r1 or r2 or c0 or c1 or c2 or diag1 or diag2:
            x_wins=True
        else:
            x_wins = False

        r0 = True if sum([1 for j in range(3) if board[0][j]==o])==3 else False
        r1 = True if sum([1 for j in range(3) if board[1][j]==o])==3 else False
        r2 = True if sum([1 for j in range(3) if board[2][j]==o])==3 else False
        c0 = True if sum([1 for i in range(3) if board[i][0]==o])==3 else False
        c1 = True if sum([1 for i in range(3) if board[i][1]==o])==3 else False
        c2 = True if sum([1 for i in range(3) if board[i][2]==o])==3 else False
        diag1 = True if sum([1 for i in range(3) for j in range(3) if board[i][j]==o and i==j])==3 else False
        diag2 = True if sum([1 for i in range(3) for j in range(3) if board[i][j]==o and i+j==2])==3 else False

        if r0 or r1 or r2 or c0 or c1 or c2 or diag1 or diag2:
            o_wins=True
        else:
            o_wins = False
        if x_wins and o_wins:
            return 'xo'
        if x_wins: return 'x'
        if o_wins: return 'o'
        return 'no_one'
    def validTicTacToe(self, board: List[str]) -> bool:
        converted_board = [[0]*3 for _ in range(3)]
        x=self.X
        o=self.O
        for i in range(3):
            for j in range(3):
                if board[i][j]=="X": converted_board[i][j]=x
                elif board[i][j]=="O": converted_board[i][j]=o

        x_count = sum([1 for i in range(3) for j in range(3) if converted_board[i][j]==x])
        o_count = sum([1 for i in range(3) for j in range(3) if converted_board[i][j]==o])
        if o_count>x_count: return False
        if x_count>o_count+1: return False

        winner = self.check_if_wins(converted_board)
        if winner=='xo': return False # both wins
        if winner=='x' and x_count==o_count: return False
        if winner=='o' and not x_count==o_count: return False
        return True


class tester(unittest.TestCase):
    def test_1(self):
        board = ["O  ","   ","   "]
        Output= False
        self.assertEqual(Output,get_sol().validTicTacToe(board))
    def test_2(self):
        board = ["XOX"," X ","   "]
        Output= False
        self.assertEqual(Output,get_sol().validTicTacToe(board))
    def test_3(self):
        board = ["XXX","   ","OOO"]
        Output= False
        self.assertEqual(Output,get_sol().validTicTacToe(board))
    def test_4(self):
        board = ["XOX","O O","XOX"]
        Output= True
        self.assertEqual(Output,get_sol().validTicTacToe(board))
    def test_5(self):
        board = ["XXX","XOO","OO "]
        Output= False
        self.assertEqual(Output,get_sol().validTicTacToe(board))
