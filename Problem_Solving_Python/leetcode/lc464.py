import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def canIWin(self, n: int, desiredTotal: int) -> bool:
        dp={}
        def selectItem(items, itemNo):
            return items | (1<<itemNo)
        def selected(items, itemNo):
            temp = items & (1<<itemNo)
            if temp==0:
                return False
            return True
        def minimax(player, remaining, items): # player1 turn, remaining, masks
            if remaining<=0: return not player
            if (player, remaining, items) in dp: return dp[(player, remaining, items)]
            if player:
                for i in reversed(range(1, n + 1)):
                    if selected(items,i): continue
                    if minimax(not player, remaining - i, selectItem(items, i)):
                        dp[(player, remaining, items)] = True
                        return True
                dp[(player, remaining, items)] = False
                return False
            else:
                for i in reversed(range(1, n + 1)):
                    if selected(items,i): continue
                    if not minimax(not player, remaining - i, selectItem(items, i)):
                        dp[(player, remaining, items)] = False
                        return False
                dp[(player, remaining, items)] = True
                return True

        if n*(n+1)/2 < desiredTotal: return False # not enough stones
        if desiredTotal<=n: return True
        return minimax(True,desiredTotal,0)

class tester(unittest.TestCase):

    def test01(self):
        maxChoosableInteger = 10
        desiredTotal = 11
        Output= False
        self.assertEqual(Output, get_sol().canIWin(maxChoosableInteger, desiredTotal))

    def test02(self):
        maxChoosableInteger = 10
        desiredTotal = 0
        Output= True
        self.assertEqual(Output, get_sol().canIWin(maxChoosableInteger, desiredTotal))

    def test03(self):
        maxChoosableInteger = 10
        desiredTotal = 1
        Output= True
        self.assertEqual(Output, get_sol().canIWin(maxChoosableInteger, desiredTotal))
    def test04(self):
        maxChoosableInteger = 4
        desiredTotal = 6
        Output= True
        self.assertEqual(Output, get_sol().canIWin(maxChoosableInteger, desiredTotal))
    def test05(self):
        maxChoosableInteger = 20
        desiredTotal = 210
        Output= False
        self.assertEqual(Output, get_sol().canIWin(maxChoosableInteger, desiredTotal))
    def test06(self):
        maxChoosableInteger = 10
        desiredTotal = 40
        Output= False
        self.assertEqual(Output, get_sol().canIWin(maxChoosableInteger, desiredTotal))
    def test07(self):
        maxChoosableInteger = 18
        desiredTotal = 79
        Output= True
        self.assertEqual(Output, get_sol().canIWin(maxChoosableInteger, desiredTotal))
    def test08(self):
        maxChoosableInteger = 5
        desiredTotal = 50
        Output= False
        self.assertEqual(Output, get_sol().canIWin(maxChoosableInteger, desiredTotal))
    def test09(self):
        maxChoosableInteger = 20
        desiredTotal = 189
        Output= False
        self.assertEqual(Output, get_sol().canIWin(maxChoosableInteger, desiredTotal))
