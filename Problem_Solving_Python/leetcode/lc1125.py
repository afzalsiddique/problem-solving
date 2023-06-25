from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # bitmask is used with skills because allSelected(skills) makes sense but allSelected(people) does not
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        def turn_on(mask,i): return mask | (1<<i)
        def is_on(mask,i): return (mask>>i)&1 # returns 1 when True or 0 when False
        def allSelected(mask, n): return mask == ((1 << n) - 1)
        def canAddNewSkills(skillMask,people_i): # can add new skills to the required skillset
            if all(is_on(skillMask,skillNo) for skillNo in people[people_i]):
                return False
            return True
        def getNewMask(skillMask,people_i): # add this person's skill to the skillset
            for skillNo in people[people_i]:
                skillMask=turn_on(skillMask,skillNo)
            return skillMask


        @cache
        def dp(skillMask, people_i_start):
            if allSelected(skillMask, len(req_skills)):
                return []
            if people_i_start==len(people):
                return INVALID_RETURN
            res=INVALID_RETURN
            for people_i in range(people_i_start,len(people)):
                newMask=skillMask
                if canAddNewSkills(newMask,people_i):
                    newMask=getNewMask(newMask,people_i)

                    peopleList= dp(newMask, people_i + 1)
                    peopleList=peopleList[:]+[people_i]
                    res=min(res,peopleList,key=lambda x:len(x))

            return res

        INVALID_RETURN=[-1]*65
        skills_indices={s:i for i,s in enumerate(req_skills)}
        newPeople=[]
        for skills in people:
            li=[]
            for skill in skills:
                if skill in skills_indices:
                    li.append(skills_indices[skill])
            newPeople.append(li)
        people=newPeople
        return dp(0, 0)
class Solution2:
    # https://leetcode.com/problems/smallest-sufficient-team/discuss/334572/Python-DP-Solution
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n=len(req_skills)
        di={req_skills[i]:i for i in range(n)}
        for i in range(len(people)):
            people[i]=[di[people[i][j]] for j in range(len(people[i]))]
        dp={}
        dp[0]=[] # (key,val)->(skillMask, people_indices)
        for i in range(len(people)):
            hisSkill=0
            for skill in people[i]:
                hisSkill|=(1<<skill)
            tmp={k:v for k,v in dp.items()}
            for skillMask in tmp:
                people_indices=dp[skillMask]
                newSkill=skillMask|hisSkill
                if newSkill==skillMask: continue
                if newSkill not in dp or len(dp[newSkill])>len(people_indices)+1:
                    dp[newSkill]=people_indices+[i]
        return dp[2**n-1]
class Solution3:
    # tle
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
    def test01(self):
        self.assertEqual([1], sorted(get_sol().smallestSufficientTeam(["nodejs","reactjs"], [["nodejs"],["nodejs","reactjs"]])))
    def test02(self):
        self.assertEqual([1,2], sorted(get_sol().smallestSufficientTeam(["algorithms","math","java","reactjs","csharp","aws"], [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]])))
    def test03(self):
        self.assertEqual([0,3], sorted(get_sol().smallestSufficientTeam(["mmcmnwacnhhdd","vza","mrxyc"], [["mmcmnwacnhhdd"],[],[],["vza","mrxyc"]])))
    def test04(self):
        self.assertEqual([12,18,23], sorted(get_sol().smallestSufficientTeam(["mwobudvo","goczubcwnfze","yspbsez","pf","ey","hkq"], [[],["mwobudvo"],["hkq"],["pf"],["pf"],["mwobudvo","pf"],[],["yspbsez"],[],["hkq"],[],[],["goczubcwnfze","pf","hkq"],["goczubcwnfze"],["hkq"],["mwobudvo"],[],["mwobudvo","pf"],["pf","ey"],["mwobudvo"],["hkq"],[],["pf"],["mwobudvo","yspbsez"],["mwobudvo","goczubcwnfze"],["goczubcwnfze","pf"],["goczubcwnfze"],["goczubcwnfze"],["mwobudvo"],["mwobudvo","goczubcwnfze"],[],["goczubcwnfze"],[],["goczubcwnfze"],["mwobudvo"],[],["hkq"],["yspbsez"],["mwobudvo"],["goczubcwnfze","ey"]])))
    def test05(self):
        self.assertEqual([13, 17, 27, 32, 34, 51], sorted(get_sol().smallestSufficientTeam(["hfkbcrslcdjq","jmhobexvmmlyyzk","fjubadocdwaygs","peaqbonzgl","brgjopmm","x","mf","pcfpppaxsxtpixd","ccwfthnjt","xtadkauiqwravo","zezdb","a","rahimgtlopffbwdg","ulqocaijhezwfr","zshbwqdhx","hyxnrujrqykzhizm"], [["peaqbonzgl","xtadkauiqwravo"],["peaqbonzgl","pcfpppaxsxtpixd","zshbwqdhx"],["x","a"],["a"],["jmhobexvmmlyyzk","fjubadocdwaygs","xtadkauiqwravo","zshbwqdhx"],["fjubadocdwaygs","x","zshbwqdhx"],["x","xtadkauiqwravo"],["x","hyxnrujrqykzhizm"],["peaqbonzgl","x","pcfpppaxsxtpixd","a"],["peaqbonzgl","pcfpppaxsxtpixd"],["a"],["hyxnrujrqykzhizm"],["jmhobexvmmlyyzk"],["hfkbcrslcdjq","xtadkauiqwravo","a","zshbwqdhx"],["peaqbonzgl","mf","a","rahimgtlopffbwdg","zshbwqdhx"],["xtadkauiqwravo"],["fjubadocdwaygs"],["x","a","ulqocaijhezwfr","zshbwqdhx"],["peaqbonzgl"],["pcfpppaxsxtpixd","ulqocaijhezwfr","hyxnrujrqykzhizm"],["a","ulqocaijhezwfr","hyxnrujrqykzhizm"],["a","rahimgtlopffbwdg"],["zshbwqdhx"],["fjubadocdwaygs","peaqbonzgl","brgjopmm","x"],["hyxnrujrqykzhizm"],["jmhobexvmmlyyzk","a","ulqocaijhezwfr"],["peaqbonzgl","x","a","ulqocaijhezwfr","zshbwqdhx"],["mf","pcfpppaxsxtpixd"],["fjubadocdwaygs","ulqocaijhezwfr"],["fjubadocdwaygs","x","a"],["zezdb","hyxnrujrqykzhizm"],["ccwfthnjt","a"],["fjubadocdwaygs","zezdb","a"],[],["peaqbonzgl","ccwfthnjt","hyxnrujrqykzhizm"],["xtadkauiqwravo","hyxnrujrqykzhizm"],["peaqbonzgl","a"],["x","a","hyxnrujrqykzhizm"],["zshbwqdhx"],[],["fjubadocdwaygs","mf","pcfpppaxsxtpixd","zshbwqdhx"],["pcfpppaxsxtpixd","a","zshbwqdhx"],["peaqbonzgl"],["peaqbonzgl","x","ulqocaijhezwfr"],["ulqocaijhezwfr"],["x"],["fjubadocdwaygs","peaqbonzgl"],["fjubadocdwaygs","xtadkauiqwravo"],["pcfpppaxsxtpixd","zshbwqdhx"],["peaqbonzgl","brgjopmm","pcfpppaxsxtpixd","a"],["fjubadocdwaygs","x","mf","ulqocaijhezwfr"],["jmhobexvmmlyyzk","brgjopmm","rahimgtlopffbwdg","hyxnrujrqykzhizm"],["x","ccwfthnjt","hyxnrujrqykzhizm"],["hyxnrujrqykzhizm"],["peaqbonzgl","x","xtadkauiqwravo","ulqocaijhezwfr","hyxnrujrqykzhizm"],["brgjopmm","ulqocaijhezwfr","zshbwqdhx"],["peaqbonzgl","pcfpppaxsxtpixd"],["fjubadocdwaygs","x","a","zshbwqdhx"],["fjubadocdwaygs","peaqbonzgl","x"],["ccwfthnjt"]])))
    def test06(self):
        self.assertEqual([0,2], sorted(get_sol().smallestSufficientTeam(["java","nodejs","reactjs"], [["java"],["nodejs"],["nodejs","reactjs"]])))
    # def test7(self):
    # def test8(self):
