from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import *
def get_sol(): return TweetCounts2()
class TweetCounts:
    # buckets. 400ms
    def __init__(self):
        self.di=defaultdict(list)
    def recordTweet(self, tweetName: str, time: int) -> None:
        self.di[tweetName].append(time)
    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq=='minute':
            interval=60
        elif freq=='hour':
            interval=3600
        else:
            interval=86400
        size=((endTime-startTime)//interval)+1
        buckets=[0]*size
        for t in self.di[tweetName]:
            if startTime<=t<=endTime:
                idx=(t-startTime)//interval
                buckets[idx]+=1
        return buckets
class TweetCounts2:
    # binary search. 1700ms
    def __init__(self):
        self.di=defaultdict(SortedList)
    def recordTweet(self, tweetName: str, time: int) -> None:
        self.di[tweetName].add(time)
    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        interval = 60 if freq == 'minute' else 3600 if freq == 'hour' else 86400
        li=self.di[tweetName]
        endTime+=1 # exclusive
        curStartTime=startTime
        res=[]
        while curStartTime<endTime:
            nextStartTime=min(curStartTime+interval,endTime)
            res.append(bisect_left(li,nextStartTime)-bisect_left(li,curStartTime))
            # res.append(bisect_right(li,nextStartTime-1)-bisect_right(li,curStartTime-1)) # bisect right version
            curStartTime=nextStartTime
        return res
class TweetCounts4:
    # tle
    def __init__(self):
        self.di=defaultdict(SortedList)
    def recordTweet(self, tweetName: str, time: int) -> None:
        self.di[tweetName].add(time)
    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq=='minute':
            freq=60
        elif freq=='hour':
            freq=3600
        else:
            freq=86400
        li=self.di[tweetName]
        res=[]
        i=li.bisect_right(startTime-1)
        lastIdx=li.bisect_right(endTime)
        x=startTime+freq-1
        while i!=lastIdx:
            j=li.bisect_right(x)
            res.append(j-i)
            x+=freq
            i=j
        length=(endTime-startTime)/freq
        if length>len(res):
            if floor(length)==ceil(length):
                lengthRemaining=int(length)-len(res)
                res.extend([0]*lengthRemaining)
            else:
                lengthRemaining=int(length)+1-len(res)
                res.extend([0]*lengthRemaining)
        return res


class Tester(unittest.TestCase):
    def do_test(self,commands, inputs):
        outputs = []
        obj = ""
        for i,cmd,input in zip(range(len(inputs)),commands,inputs):
            if cmd=='TweetCounts': obj = get_sol(); outputs.append(None)
            elif cmd=='recordTweet': outputs.append(obj.recordTweet(input[0],input[1]))
            elif cmd=='getTweetCountsPerFrequency': outputs.append(obj.getTweetCountsPerFrequency(input[0],input[1],input[2],input[3]))
        return outputs
    def test_01(self):
        commands = ["TweetCounts","recordTweet","recordTweet","recordTweet","getTweetCountsPerFrequency","getTweetCountsPerFrequency","recordTweet","getTweetCountsPerFrequency"]
        inputs=[[],["tweet3",0],["tweet3",60],["tweet3",10],["minute","tweet3",0,59],["minute","tweet3",0,60],["tweet3",120],["hour","tweet3",0,210]]
        expected = [None,None,None,None,[2],[2,1],None,[4]]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test_02(self):
        commands = ["TweetCounts","recordTweet","recordTweet","recordTweet","recordTweet","recordTweet","getTweetCountsPerFrequency","recordTweet","recordTweet","recordTweet","recordTweet"]
        inputs=[[],               ["tweet0",33],["tweet1",89],["tweet2",99],["tweet3",53],["tweet4",3],["hour","tweet0",89,3045],    ["tweet0",28],["tweet0",91],["tweet0",9],["tweet1",6]]
        expected = [None,None,None,None,None,None,[0],None,None,None,None]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test_03(self):
        commands = ["TweetCounts","recordTweet","recordTweet","recordTweet","recordTweet","recordTweet","recordTweet","getTweetCountsPerFrequency","getTweetCountsPerFrequency"]
        inputs=[[],["tweet0",13],["tweet1",16],["tweet2",12],["tweet3",18],["tweet4",82],["tweet3",89],["day","tweet0",89,9471],["hour","tweet3",13,4024]]
        expected = [None,None,None,None,None,None,None,[0],[2,0]]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)
    def test_04(self):
        commands = ["TweetCounts","recordTweet","recordTweet","recordTweet","recordTweet","recordTweet","recordTweet","recordTweet","recordTweet","getTweetCountsPerFrequency","recordTweet"]
        inputs=[[],["tweet0",15],["tweet1",99],["tweet2",77],["tweet3",27],["tweet4",86],["tweet4",58],["tweet1",74],["tweet4",89],["hour","tweet3",74,5573],["tweet2",81]]
        expected = [None,None,None,None,None,None,None,None,None,[0,0],None]
        outputs = self.do_test(commands, inputs)
        self.assertEqual(expected,outputs)


