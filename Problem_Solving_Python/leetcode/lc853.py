import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # https://www.youtube.com/watch?v=H5w6doOXz10
    # greedy
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed),reverse=True)
        time=[]
        for pos,speed in cars:
            distance_left=target-pos
            time_to_reach_destination = distance_left/speed
            time.append(time_to_reach_destination)

        cur_time=-1
        fleet=0
        for t in time:
            if t>cur_time:
                fleet+=1
                cur_time=t
        return fleet
class Solution2:
    # wrong
    # tried brute force
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        EMPTY = -1
        def empty(road):
            for x in road:
                if x!=-1: return False
            return True
        def move_car(road,i):
            if i+speed[road[i]]>=target: # goes to finish line
                road[-1]=road[i] # move to finish line
                road[i]=EMPTY # empty the space where it moved "FROM"
                return
            for j in range(i+1,i+speed[road[i]]+1):
                if road[j]!=EMPTY:
                    if speed[road[i]]<speed[road[j]]:
                        road[j]=i
                    else:
                        road[j]=j
                    road[j]=EMPTY
                    return
            road[i+speed[road[i]]]=road[i]
            road[i]=EMPTY

        road = [-1]*(target+1)
        for i,pos in enumerate(position):
            road[pos]=i
        cnt=0
        while not empty(road):
            if road[-1]!=EMPTY: # finishing line not empty
                cnt+=1
            road[-1]=EMPTY # clear the finishing line
            for i in reversed(range(target+1)):
                if road[i]==EMPTY: continue
                move_car(road,i)
        return cnt


class tester(unittest.TestCase):
    def test01(self):
        target = 12
        position = [10,8,0,5,3]
        speed = [2,4,1,1,3]
        Output= 3
        self.assertEqual(Output,get_sol().carFleet(target,position,speed))
    def test02(self):
        target = 10
        position = [8,3,7,4,6,5]
        speed = [4,4,4,4,4,4]
        Output= 3
        self.assertEqual(Output,get_sol().carFleet(target,position,speed))
    # def test03(self):
    # def test04(self):
    # def test05(self):
