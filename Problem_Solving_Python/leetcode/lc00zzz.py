from itertools import accumulate,permutations; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, cmp_to_key; from heapq import heappop,heappush,heapify; import unittest; from typing import List, Optional, Union; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des,TreeNode; from a_linked_list import make_linked_list
from Problem_Solving_Python.template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        def turn_on(mask,i): return mask | (1<<i)
        def is_on(mask,i): return (mask>>i)&1 # returns 1 when True or 0 when False
        def allSelected(mask, n): return mask == ((1 << n) - 1)
        @cache
        def dp(i,mask):
            if i==n:
                if allSelected(mask,n):
                    return 0
                return float('inf')
            res=float('inf')
            for peopleSkills in people:
                newMask=mask
                hasAtLeastOneNewSkill=False
                for skillNo in peopleSkills:
                    hasAtLeastOneNewSkill=True
                    if not is_on(newMask,skillNo):
                        newMask=turn_on(newMask,skillNo)
                if hasAtLeastOneNewSkill:
                    res=min(res,1+dp(i+1,newMask))
                res=min(res,dp(i+1,mask))
            return res

        n=len(req_skills)
        skills_indices={s:i for i,s in enumerate(req_skills)}
        newPeople=[]
        for skills in people:
            li=[]
            for skill in skills:
                if skill in skills_indices:
                    li.append(skills_indices[skill])
            newPeople.append(li)
        people=newPeople
        return dp(0,0)

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual([0,2], get_sol().smallestSufficientTeam(["java","nodejs","reactjs"], [["java"],["nodejs"],["nodejs","reactjs"]]))
    def test2(self):
        self.assertEqual([1,2], get_sol().smallestSufficientTeam(["algorithms","math","java","reactjs","csharp","aws"], [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]))
    def test3(self):
        self.assertEqual([0,3], get_sol().smallestSufficientTeam(["mmcmnwacnhhdd","vza","mrxyc"], [["mmcmnwacnhhdd"],[],[],["vza","mrxyc"]]))
    def test4(self):
        self.assertEqual([12,18,23], get_sol().smallestSufficientTeam(["mwobudvo","goczubcwnfze","yspbsez","pf","ey","hkq"], [[],["mwobudvo"],["hkq"],["pf"],["pf"],["mwobudvo","pf"],[],["yspbsez"],[],["hkq"],[],[],["goczubcwnfze","pf","hkq"],["goczubcwnfze"],["hkq"],["mwobudvo"],[],["mwobudvo","pf"],["pf","ey"],["mwobudvo"],["hkq"],[],["pf"],["mwobudvo","yspbsez"],["mwobudvo","goczubcwnfze"],["goczubcwnfze","pf"],["goczubcwnfze"],["goczubcwnfze"],["mwobudvo"],["mwobudvo","goczubcwnfze"],[],["goczubcwnfze"],[],["goczubcwnfze"],["mwobudvo"],[],["hkq"],["yspbsez"],["mwobudvo"],["goczubcwnfze","ey"]]))
    def test5(self):
        self.assertEqual([13, 17, 27, 32, 34, 51], get_sol().smallestSufficientTeam(["hfkbcrslcdjq","jmhobexvmmlyyzk","fjubadocdwaygs","peaqbonzgl","brgjopmm","x","mf","pcfpppaxsxtpixd","ccwfthnjt","xtadkauiqwravo","zezdb","a","rahimgtlopffbwdg","ulqocaijhezwfr","zshbwqdhx","hyxnrujrqykzhizm"], [["peaqbonzgl","xtadkauiqwravo"],["peaqbonzgl","pcfpppaxsxtpixd","zshbwqdhx"],["x","a"],["a"],["jmhobexvmmlyyzk","fjubadocdwaygs","xtadkauiqwravo","zshbwqdhx"],["fjubadocdwaygs","x","zshbwqdhx"],["x","xtadkauiqwravo"],["x","hyxnrujrqykzhizm"],["peaqbonzgl","x","pcfpppaxsxtpixd","a"],["peaqbonzgl","pcfpppaxsxtpixd"],["a"],["hyxnrujrqykzhizm"],["jmhobexvmmlyyzk"],["hfkbcrslcdjq","xtadkauiqwravo","a","zshbwqdhx"],["peaqbonzgl","mf","a","rahimgtlopffbwdg","zshbwqdhx"],["xtadkauiqwravo"],["fjubadocdwaygs"],["x","a","ulqocaijhezwfr","zshbwqdhx"],["peaqbonzgl"],["pcfpppaxsxtpixd","ulqocaijhezwfr","hyxnrujrqykzhizm"],["a","ulqocaijhezwfr","hyxnrujrqykzhizm"],["a","rahimgtlopffbwdg"],["zshbwqdhx"],["fjubadocdwaygs","peaqbonzgl","brgjopmm","x"],["hyxnrujrqykzhizm"],["jmhobexvmmlyyzk","a","ulqocaijhezwfr"],["peaqbonzgl","x","a","ulqocaijhezwfr","zshbwqdhx"],["mf","pcfpppaxsxtpixd"],["fjubadocdwaygs","ulqocaijhezwfr"],["fjubadocdwaygs","x","a"],["zezdb","hyxnrujrqykzhizm"],["ccwfthnjt","a"],["fjubadocdwaygs","zezdb","a"],[],["peaqbonzgl","ccwfthnjt","hyxnrujrqykzhizm"],["xtadkauiqwravo","hyxnrujrqykzhizm"],["peaqbonzgl","a"],["x","a","hyxnrujrqykzhizm"],["zshbwqdhx"],[],["fjubadocdwaygs","mf","pcfpppaxsxtpixd","zshbwqdhx"],["pcfpppaxsxtpixd","a","zshbwqdhx"],["peaqbonzgl"],["peaqbonzgl","x","ulqocaijhezwfr"],["ulqocaijhezwfr"],["x"],["fjubadocdwaygs","peaqbonzgl"],["fjubadocdwaygs","xtadkauiqwravo"],["pcfpppaxsxtpixd","zshbwqdhx"],["peaqbonzgl","brgjopmm","pcfpppaxsxtpixd","a"],["fjubadocdwaygs","x","mf","ulqocaijhezwfr"],["jmhobexvmmlyyzk","brgjopmm","rahimgtlopffbwdg","hyxnrujrqykzhizm"],["x","ccwfthnjt","hyxnrujrqykzhizm"],["hyxnrujrqykzhizm"],["peaqbonzgl","x","xtadkauiqwravo","ulqocaijhezwfr","hyxnrujrqykzhizm"],["brgjopmm","ulqocaijhezwfr","zshbwqdhx"],["peaqbonzgl","pcfpppaxsxtpixd"],["fjubadocdwaygs","x","a","zshbwqdhx"],["fjubadocdwaygs","peaqbonzgl","x"],["ccwfthnjt"]]))
    # def test6(self):
    # def test7(self):
    # def test8(self):
