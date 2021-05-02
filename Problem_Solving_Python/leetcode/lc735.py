# https://www.youtube.com/watch?v=ksbXEzEAg1U
import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List

class Solution:
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



def get_sol_obj(): return Solution()
class tester(unittest.TestCase):
    def test1(self):
        asteroids= [8,6,-9]
        Output= [-9]
        self.assertEqual(Output,get_sol_obj().asteroidCollision(asteroids))
    def test1_2(self):
        asteroids= [8,6,-8]
        Output= []
        self.assertEqual(Output,get_sol_obj().asteroidCollision(asteroids))
    def test2(self):
        asteroids = [5,10,-5]
        Output= [5,10]
        self.assertEqual(Output,get_sol_obj().asteroidCollision(asteroids))
    def test3(self):
        asteroids = [8,-8]
        Output= []
        self.assertEqual(Output,get_sol_obj().asteroidCollision(asteroids))
    def test4(self):
        asteroids = [10,2,-5]
        Output= [10]
        self.assertEqual(Output,get_sol_obj().asteroidCollision(asteroids))
    def test5(self):
        asteroids = [-2,-1,1,2]
        Output= [-2,-1,1,2]
        self.assertEqual(Output,get_sol_obj().asteroidCollision(asteroids))
    def test6(self):
        asteroids = [5,4,3,2,1,-4]
        Output= [5]
        self.assertEqual(Output,get_sol_obj().asteroidCollision(asteroids))
