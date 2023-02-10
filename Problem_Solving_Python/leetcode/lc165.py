from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def compareVersion(self, s1: str, s2: str) -> int:
        m,n= len(s1), len(s2)
        i,j=0,0
        while i<m or j<n:
            ver1,ver2=0,0
            while i<m and s1[i]!='.':
                ver1=ver1*10+ord(s1[i])-ord('0')
                i+=1
            while j<n and s2[j]!='.':
                ver2=ver2*10+ord(s2[j])-ord('0')
                j+=1
            i+=1
            j+=1
            if ver1>ver2:
                return 1
            if ver2>ver1:
                return -1
        return 0
class Solution2:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1=[int(x) for x in version1.split('.')]
        version2=[int(x) for x in version2.split('.')]
        while len(version1)<len(version2):
            version1.append(0)
        while len(version2)<len(version1):
            version2.append(0)
        if version1>version2:
            return 1
        elif version1<version2:
            return -1
        return 0

class Solution3:
    def compareVersion(self, v1: str, v2: str) -> int:
        if len(v1)<len(v2): # v1 longer or equal
            return (-1)*self.compareVersion(v2,v1) # multiply with -1. because we are flipping the order

        v1 = list(map(int,v1.split('.')))
        v2 = list(map(int,v2.split('.')))

        i=0
        while i<len(v2): # iterate upto the length of smaller version
            if v1[i]>v2[i]:
                return 1
            elif v1[i]<v2[i]:
                return -1
            i+=1

        while i<len(v1): # iterate upto the length of longer version
            if v1[i]>0:
                return 1
            i+=1

        return 0


class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(0, get_sol().compareVersion( "1.01",  "1.001"))
    def test02(self):
        self.assertEqual(0, get_sol().compareVersion( "1.0",  "1.0.0"))
    def test03(self):
        self.assertEqual(-1, get_sol().compareVersion( "0.1",  "1.1"))
    def test04(self):
        self.assertEqual(1, get_sol().compareVersion( "1.0.1",  "1"))
    def test05(self):
        self.assertEqual(-1, get_sol().compareVersion( "7.5.2.4",  "7.5.3"))
    def test06(self):
        self.assertEqual(-1, get_sol().compareVersion( "1.0",  "1.0.1"))
