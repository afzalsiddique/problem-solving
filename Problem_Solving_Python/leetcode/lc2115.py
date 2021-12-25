import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        def valid(i:int):
            for ing in ingredients[i]:
                if ing not in supplies:
                    return False
            return True
        def oneFound():
            for i in range(len(recipes)):
                if valid(i):
                    return i
            return -1

        supplies=set(supplies)
        res=[]
        while True:
            i = oneFound()
            if i==-1:
                break
            res.append(recipes[i])
            supplies.add(recipes[i])
            recipes=recipes[:i]+recipes[i+1:]
            ingredients=ingredients[:i]+ingredients[i+1:]
        return res


class Tester(unittest.TestCase):
    def test1(self):
        self.assertEqual(["bread"], get_sol().findAllRecipes(recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]))
    def test2(self):
        self.assertEqual(["bread","sandwich"], get_sol().findAllRecipes(recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]))
    def test3(self):
        self.assertEqual(["bread","sandwich","burger"], get_sol().findAllRecipes(recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]))
    # def test4(self):
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
