import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # bitmask
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        def turn_on(jobs,job_id):
            return jobs|1<<job_id
        def is_subset(job1,job2):  # if job1 is a subset of job2
            return job1 == job2&job1
        n=len(favoriteCompanies)

        j=0
        comp_di={} # companies with their ids
        for i in range(n):
            for comp in favoriteCompanies[i]:
                if comp not in comp_di:
                    comp_di[comp]=j
                    j+=1

        li = [0]*n
        for i in range(n):
            for comp in favoriteCompanies[i]:
                li[i]=turn_on(li[i],comp_di[comp])

        res = []
        for i in range(n):
            flag=True
            for j in range(n):
                if i==j: continue
                if is_subset(li[i],li[j]):
                    flag=False
                    break
            if flag: res.append(i)
        return res
class Solution2:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        def is_subset(i):
            for j in range(n):
                flag=True
                if j==i: continue
                for comp in li[i]:
                    if comp not in li[j]:
                        flag=False
                        break
                if flag: return True
            return False

        n=len(favoriteCompanies)
        li=[set(comp) for comp in favoriteCompanies]
        res=[i for i in range(n) if not is_subset(i)]
        return res

class Tester(unittest.TestCase):
    def test_1(self):
        favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
        Output= [0,1,4]
        self.assertEqual(Output,get_sol().peopleIndexes(favoriteCompanies))
    def test_2(self):
        favoriteCompanies = [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]
        Output= [0,1]
        self.assertEqual(Output,get_sol().peopleIndexes(favoriteCompanies))
    def test_3(self):
        favoriteCompanies = [["leetcode"],["google"],["facebook"],["amazon"]]
        Output= [0,1,2,3]
        self.assertEqual(Output,get_sol().peopleIndexes(favoriteCompanies))
    # def test_4(self):
    # def test_5(self):
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):
