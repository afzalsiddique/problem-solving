import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def if_warning(times:List[int]):
            n=len(times)
            for i in range(2,n):
                if times[i]-times[i-2]<=100:
                    return True
            return False
        def convert_time(time:str):
            # '23:00' to 2300
            return int(time[0]+time[1]+time[3]+time[4])
        res=set()
        keyTime = [convert_time(x) for x in keyTime]
        di=defaultdict(list)
        for i,[name,time] in enumerate(zip(keyName,keyTime)):
            di[name].append(time)
        for name in di:
            di[name].sort()
            if if_warning(di[name]):
                res.add(name)
        return sorted(res)


class MyTestCase(unittest.TestCase):
    def test_1(self):
        keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"]
        keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
        Output= ["daniel"]
        self.assertEqual(Output, get_sol().alertNames(keyName,keyTime))
    def test_2(self):
        keyName = ["alice","alice","alice","bob","bob","bob","bob"]
        keyTime = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]
        Output= ["bob"]
        self.assertEqual(Output, get_sol().alertNames(keyName,keyTime))
    def test_3(self):
        keyName = ["john","john","john"]
        keyTime = ["23:58","23:59","00:01"]
        Output= []
        self.assertEqual(Output, get_sol().alertNames(keyName,keyTime))
    def test_4(self):
        keyName = ["leslie","leslie","leslie","clare","clare","clare","clare"]
        keyTime = ["13:00","13:20","14:00","18:00","18:51","19:30","19:49"]
        Output= ["clare","leslie"]
        self.assertEqual(Output, get_sol().alertNames(keyName,keyTime))
    def test_5(self):
        keyName = ["a","a","a","a","a","a","b","b","b","b","b"]
        keyTime = ["23:27","03:14","12:57","13:35","13:18","21:58","22:39","10:49","19:37","14:14","10:41"]
        Output= ["a"]
        self.assertEqual(Output, get_sol().alertNames(keyName,keyTime))
    def test_6(self):
        keyName = ["a","a","a","a","a","a"]
        keyTime = ["23:27","03:14","12:57","13:35","13:18","21:58"]
        Output= ["a"]
        self.assertEqual(Output, get_sol().alertNames(keyName,keyTime))
    # def test_7(self):
    # def test_8(self):
    # def test_9(self):