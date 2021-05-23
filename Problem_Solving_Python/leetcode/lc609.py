import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=4KGl6PMwVXE
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        di=defaultdict(list)
        for path in paths:
            arr = path.split()
            dir=arr[0]
            for i in range(1,len(arr)):
                start,end=0,arr[i].index('(')
                filename=arr[i][start:end]
                start,end=arr[i].index('(')+1, len(arr[i])-1
                content = arr[i][start:end]
                di[content].append(dir+'/'+filename)
        # format res
        res=[]
        for content in di:
            if len(di[content])>1:
                res.append(di[content])
        return res


class tester(unittest.TestCase):
    def test01(self):
        paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
        Output= [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
        self.assertEqual(Output, get_sol().findDuplicate(paths))
    def test02(self):
        paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]
        Output= [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]
        self.assertEqual(Output, get_sol().findDuplicate(paths))
