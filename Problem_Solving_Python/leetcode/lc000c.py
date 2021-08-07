import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        n=len(students)
        self.maxx=0
        vis=set()
        dp_score={}
        def get_score(stu_i,men_i):
            if (stu_i,men_i) in dp_score: return dp_score[stu_i,men_i]
            cnt= sum(students[stu_i][i]==mentors[men_i][i] for i in range(len(students[0])))
            dp_score[stu_i,men_i]=cnt
            return cnt
        def h(start, score):
            self.maxx=max(self.maxx,score)
            for i in range(start,n):
                for j in range(n):
                    if j in vis: continue
                    vis.add(j)
                    h(i+1,score+get_score(i,j))
                    vis.remove(j)

        h(0,0)
        return self.maxx




class tester(unittest.TestCase):
    def test_1(self):
        students = [[1,1,0],[1,0,1],[0,0,1]]
        mentors = [[1,0,0],[0,0,1],[1,1,0]]
        Output= 8
        self.assertEqual(Output, get_sol().maxCompatibilitySum(students,mentors))
    def test_2(self):
        students = [[0,0],[0,0],[0,0]]
        mentors = [[1,1],[1,1],[1,1]]
        Output= 0
        self.assertEqual(Output, get_sol().maxCompatibilitySum(students,mentors))
    def test_3(self):
        students = [[0,1,0,0,0,0,0,1],[1,1,1,0,1,0,1,1],[1,1,1,0,0,1,1,1],[0,1,0,1,0,0,0,0],[1,0,0,0,1,0,1,0],[1,1,1,1,0,1,1,1],[1,1,1,1,1,0,0,1],[0,1,0,1,0,0,1,1]]
        mentors = [[1,1,1,1,1,1,1,0],[0,0,0,0,0,1,0,1],[1,0,1,1,1,1,0,1],[0,1,1,1,0,0,1,1],[0,0,0,1,1,0,1,0],[1,0,1,0,1,0,0,0],[1,0,1,1,1,1,0,0],[0,0,0,0,0,1,0,1]]
        Output= 43
        self.assertEqual(Output, get_sol().maxCompatibilitySum(students,mentors))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
