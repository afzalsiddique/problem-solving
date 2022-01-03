import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
# from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/smallest-sufficient-team/discuss/334572/Python-DP-Solution
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n=len(req_skills)
        di={req_skills[i]:i for i in range(n)}
        for i in range(len(people)):
            people[i]=[di[people[i][j]] for j in range(len(people[i]))]
        dp={}
        dp[0]=[]
        for i in range(len(people)):
            hisSkill=0
            for skill in people[i]:
                hisSkill|=(1<<skill)
            tmp={k:v for k,v in dp.items()}
            for skillSet in tmp:
                need=dp[skillSet]
                newSkill=skillSet|hisSkill
                if newSkill==skillSet: continue
                if newSkill not in dp or len(dp[newSkill])>len(need)+1:
                    dp[newSkill]=need+[i]
        return dp[2**n-1]
class Solution3:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        def turnOn(mask:int,ithPeople:int):
            for j in people[ithPeople]:
                mask=mask|(1<<j)
            return mask
        def isOn(mask:int,i:int):
            return mask&(1<<i)
        def needPerson(i:int,mask:int):
            for j in people[i]:
                if not isOn(mask,j):
                    return True
            return False
        def dfs(start:int,mask:int,path):
            nonlocal res
            if mask==goal:
                res=min(res,path,key=lambda x:len(x))
                return
            for i in range(start,len(people)):
                if needPerson(i,mask):
                    dfs(start,turnOn(mask,i),path+[i])

        n=len(req_skills)
        goal=2**n-1
        res=[-1]*17
        di={req_skills[i]:i for i in range(n)}
        for i in range(len(people)):
            people[i]=[di[people[i][j]] for j in range(len(people[i]))]
        dfs(0,0,[])
        return res
class Solution4:
    # tle
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        def selectPerson(i:int,selected:set[int]):
            return selected | (set(people[i]))
        def needPerson(i:int):
            for skill in people[i]:
                if skill not in selected:
                    return True
            return False
        def dfs(start:int,selected:set[int],path:List[int]):
            nonlocal res
            if len(selected)==n:
                res=min(res,path,key=lambda x:len(x))
            for i in range(start,len(people)):
                if needPerson(i):
                    tmp=selectPerson(i,selected)
                    dfs(i+1,tmp,path+[i])

        n=len(req_skills)
        di={req_skills[i]:i for i in range(n)}
        for i in range(len(people)):
            people[i]=[di[people[i][j]] for j in range(len(people[i]))]
        res=[-1]*17
        selected=set()
        dfs(0,set(),[])
        return res

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual([0,2], get_sol().smallestSufficientTeam(["java","nodejs","reactjs"], [["java"],["nodejs"],["nodejs","reactjs"]]))
    def test2(self):
        self.assertEqual([1,2], get_sol().smallestSufficientTeam(["algorithms","math","java","reactjs","csharp","aws"], [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]))
    def test3(self):
        self.assertEqual([0,3], get_sol().smallestSufficientTeam(["mmcmnwacnhhdd","vza","mrxyc"], [["mmcmnwacnhhdd"],[],[],["vza","mrxyc"]]))
    def test4(self):
        self.assertEqual([12,18,23], get_sol().smallestSufficientTeam(["mwobudvo","goczubcwnfze","yspbsez","pf","ey","hkq"], [[],["mwobudvo"],["hkq"],["pf"],["pf"],["mwobudvo","pf"],[],["yspbsez"],[],["hkq"],[],[],["goczubcwnfze","pf","hkq"],["goczubcwnfze"],["hkq"],["mwobudvo"],[],["mwobudvo","pf"],["pf","ey"],["mwobudvo"],["hkq"],[],["pf"],["mwobudvo","yspbsez"],["mwobudvo","goczubcwnfze"],["goczubcwnfze","pf"],["goczubcwnfze"],["goczubcwnfze"],["mwobudvo"],["mwobudvo","goczubcwnfze"],[],["goczubcwnfze"],[],["goczubcwnfze"],["mwobudvo"],[],["hkq"],["yspbsez"],["mwobudvo"],["goczubcwnfze","ey"]]))
    # def test5(self):
    # def test6(self):
    # def test7(self):
    # def test8(self):
