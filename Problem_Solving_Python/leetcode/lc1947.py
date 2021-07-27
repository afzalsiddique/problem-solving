import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m, n = len(students), len(students[0])
        mentors_vis = [False]* m
        def calculate_score(s_id, m_id):
            return sum(students[s_id][i]==mentors[m_id][i] for i in range(n))

        score_cache=[[0]*m for _ in range(m)]
        for s_id in range(m):
            for m_id in range(m):
                score_cache[s_id][m_id]=calculate_score(s_id,m_id)

        def get_score(s_id,m_id): return score_cache[s_id][m_id]

        def select_next_stu(s_id, score):
            if s_id==m: return score
            maxx=0
            for m_id in range(m):
                if mentors_vis[m_id]: continue
                mentors_vis[m_id]=True
                maxx=max(maxx, select_next_stu(s_id+1, score+get_score(s_id,m_id)))
                mentors_vis[m_id]=False
            return maxx

        return select_next_stu(0,0)
class Solution2:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m, n = len(students), len(students[0])
        mentors_vis = [False]* m
        def get_score(s_id, m_id):
            return sum(students[s_id][i]==mentors[m_id][i] for i in range(n))

        def select_next_stu(s_id, score):
            if s_id==m: return score
            maxx=0
            for m_id in range(m):
                if mentors_vis[m_id]: continue
                mentors_vis[m_id]=True
                maxx=max(maxx, select_next_stu(s_id+1, score+get_score(s_id,m_id)))
                mentors_vis[m_id]=False
            return maxx

        return select_next_stu(0,0)
class Solution3:
    # tle
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
    def test_4(self):
        students = [[0,1,1,1,1],[1,0,0,0,0],[1,0,1,1,1],[1,1,0,1,1],[1,0,1,1,0],[0,1,0,0,0],[0,1,1,0,0],[1,1,0,1,1]]
        mentors = [[0,0,0,1,0],[0,0,0,0,1],[0,1,0,0,1],[0,1,1,1,0],[1,0,0,1,1],[1,1,1,1,0],[1,1,1,1,0],[0,1,1,1,0]]
        Output= 28
        self.assertEqual(Output, get_sol().maxCompatibilitySum(students,mentors))
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
