from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class UnionFind:
    def __init__(self):
        self.par={}
        self.size={}
    def __repr__(self): return str(self.par)
    def add(self,a):
        if a not in self.par:
            self.par[a]=a
            self.size[a]=1
    def union(self,a,b):
        self.add(a),self.add(b)
        a=self.find(a)
        b=self.find(b)
        if a!=b:
            if self.size[a]<self.size[b]:
                a,b=b,a
            self.par[b]=a
            self.size[a]+=self.size[b]
    def find(self,a):
        self.add(a)
        if a!=self.par[a]:
            self.par[a]=self.find(self.par[a])
        return self.par[a]
    def unionAll(self,li):
        if len(li)<1: return
        first=li[0]
        for second in li[1:]:
            self.union(first,second)
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emailToName={}
        uf=UnionFind()
        for a in accounts:
            name=a[0]
            for email in a[1:]:
                emailToName[email]=name
            uf.unionAll(a[1:])

        di=defaultdict(list)
        for email in emailToName:
            rep_email=uf.find(email)
            di[rep_email].append(email)
        for email in di:
            di[email].sort()

        res=[]
        for rep_email in di:
            name=emailToName[rep_email]
            li=[name]+di[rep_email]
            res.append(li)
        return res

class Solution2:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}

        def add(name, email):
            if email not in parent:
                parent[email] = (name, email)

        def find(name, email):
            if email in parent:
                p = parent[email]
            else:
                p = (name, email)
            if (name, email)==p:
                return p

            par_name, par_email = parent[email]
            parent[email] = find(par_name, par_email)
            return parent[email]

        def union(name1, email1, name2, email2):
            add(name1, email1), add(name2, email2)
            p1, p2 = find(name1, email1), find(name2, email2)
            if p1!=p2:
                temp_email1, temp_email2 = p1[1], p2[1]
                parent[temp_email1] = parent[temp_email2]

        for account in accounts:
            name = account[0]
            emails = account[1:]
            for i,email in enumerate(emails):
                add(name, email)
                if i==0:
                    continue
                union(name, email, name, emails[i-1])


        # the dictionary looks like this : {('John', '1'): {'1', '2', '3'}, ('John', '101'): {'101'}, ('Mary', '999'): {'999'}})
        res = defaultdict(set)
        for account in accounts:
            emails = account[1:]
            for i, email in enumerate(emails):
                temp_par_name, temp_par_email = parent[email]
                true_par_name, true_par_email = find(temp_par_name, temp_par_email)
                res[(true_par_name,true_par_email)].add(email)



        res_list = [] # convert dictionary to list
        for name, email in res:
            temp = [name] + sorted(list(res[(name,email)]))
            res_list.append(temp)
        return res_list




class MyTestCase(unittest.TestCase):
    def test01(self):
        expected = [["John",'1', '2', '3'],  ["John", "101"], ["Mary", "999"]]
        self.assertEqual(expected, get_sol().accountsMerge([["John", "1", "2"], ["John", "101"], ["John", "1", "3"], ["Mary", "999"]]))
    def test02(self):
        expected = [["Ethan","1","2","3"],["Gabe","4","5","6"],["Hanzo","7","8","9"],["Kevin","10","11","12"],["Fern","13","14","15"]]
        self.assertEqual(expected, get_sol().accountsMerge([["Gabe","4","6","5"],["Kevin","11","12","10"],["Ethan","3","2","1"],["Hanzo","9","8","7"],["Fern","15","14","13"]]))
