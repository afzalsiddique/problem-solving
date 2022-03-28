from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
def get_sol(): return Solution()
# https://www.youtube.com/watch?v=ksbXEzEAg1U

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        res=[]
        for stone in asteroids:
            if stone>0:
                st.append(stone)
            else:
                while st and st[-1]<abs(stone):
                    st.pop()
                if st:
                    if st[-1]==abs(stone):
                        st.pop()
                        continue
                else:
                    res.append(stone)
        res.extend(st)
        return res
class Solution3:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        res = []
        for x in asteroids:
            if x>0:
                st.append(x)
            else:
                if not st:
                    res.append(x)
                else:
                    while st and st[-1]<abs(x):
                        st.pop()
                    if not st: # [8,6,-9]
                        res.append(x)
                    if st and st[-1]==abs(x):
                        st.pop()
        return res+st
class Solution2:
    def asteroidCollision(self, asteroids):
        st = []
        for ast in asteroids:
            st.append(ast)
            while len(st) > 1 and st[-1] < 0 and st[-2] > 0:
                if st[-1] + st[-2] < 0: st.pop(-2)
                elif st[-1] + st[-2] > 0: st.pop()
                else:
                    st.pop(); st.pop()
                    break

        return st

class Solution3:
    def asteroidCollision(self, asteroids):
        st = []
        for num in asteroids:
            if num>0:
                st.append(num)
            else:
                while st and st[-1]>0 and st[-1]<abs(num): # case: [5,4,3,2,1,-4]
                    st.pop()
                if not st or st[-1]<0:
                    st.append(num)
                elif st[-1] == abs(num): # [8,-8]
                    st.pop()
        return st



class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual([-9], get_sol().asteroidCollision([8,6,-9]))
    def test02(self):
        self.assertEqual([], get_sol().asteroidCollision([8,6,-8]))
    def test03(self):
        self.assertEqual([5,10], get_sol().asteroidCollision([5,10,-5]))
    def test04(self):
        self.assertEqual([], get_sol().asteroidCollision([8,-8]))
    def test05(self):
        self.assertEqual([10], get_sol().asteroidCollision([10,2,-5]))
    def test06(self):
        self.assertEqual([-2,-1,1,2], get_sol().asteroidCollision([-2,-1,1,2]))
    def test07(self):
        self.assertEqual([5], get_sol().asteroidCollision([5,4,3,2,1,-4]))
    def test08(self):
        self.assertEqual([-2,1], get_sol().asteroidCollision([-2,1,1,-1]))
