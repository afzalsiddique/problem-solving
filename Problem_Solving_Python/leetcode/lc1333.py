import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        def filt(x):
            _,rating,friendly,price,dist=x
            if veganFriendly and not friendly: return False
            if price>maxPrice: return False
            if dist>maxDistance: return False
            return True

        li = list(filter(filt,restaurants))
        li.sort(key=lambda x:(-x[1],-x[0]))
        res=[x[0] for x in li]
        return res
class Tester(unittest.TestCase):
    def test_1(self):
        restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]
        veganFriendly = 1
        maxPrice = 50
        maxDistance = 10
        Output= [3,1,5]
        self.assertEqual(Output,get_sol().filterRestaurants(restaurants,veganFriendly,maxPrice,maxDistance))
    def test_2(self):
        restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]
        veganFriendly = 0
        maxPrice = 50
        maxDistance = 10
        Output= [4,3,2,1,5]
        self.assertEqual(Output,get_sol().filterRestaurants(restaurants,veganFriendly,maxPrice,maxDistance))
    def test_3(self):
        restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]
        veganFriendly = 0
        maxPrice = 30
        maxDistance = 3
        Output= [4,5]
        self.assertEqual(Output,get_sol().filterRestaurants(restaurants,veganFriendly,maxPrice,maxDistance))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):