import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        permutations=[]
        def permute(arr:List[str],path):
            if not arr:
                permutations.append(''.join(path[:]))
                return
            for i in range(len(arr)):
                permute(arr[:i]+arr[i+1:],path+[arr[i]])
        def valid(time:str):
            hours=time[:2]
            minutes=time[2:]
            if '00'<=hours<='23' and '00'<=minutes<='59': return True
            return False

        arr = list(map(str,arr))
        permute(arr,[])
        maxx=''
        for time in permutations:
            if valid(time) and time>maxx:
                    maxx=time
        if maxx=='': return ''
        return maxx[:2]+':'+maxx[2:]

class tester(unittest.TestCase):
    def test01(self):
        arr = [1,2,3,4]
        Output= "23:41"
        self.assertEqual(Output, get_sol().largestTimeFromDigits(arr))
    def test02(self):
        arr = [5,5,5,5]
        Output= ""
        self.assertEqual(Output, get_sol().largestTimeFromDigits(arr))
    def test03(self):
        arr = [0,0,0,0]
        Output= "00:00"
        self.assertEqual(Output, get_sol().largestTimeFromDigits(arr))
    def test04(self):
        arr = [0,0,1,0]
        Output= "10:00"
        self.assertEqual(Output, get_sol().largestTimeFromDigits(arr))
    def test05(self):
        arr = [1,9,6,0]
        Output= "19:06"
        self.assertEqual(Output, get_sol().largestTimeFromDigits(arr))
