import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n=len(people)
        people.sort()
        left,right=0,n-1
        cnt=0
        while left<=right:
            if left==right:
                cnt+=1
                break
            if people[left]+people[right]<=limit:
                left+=1
                right-=1
            else:
                right-=1
            cnt+=1
        return cnt


class Solution2:
    # wrong
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        cnt=0
        people.sort()
        temp=0
        for i in range(len(people)):
            if temp==0: # no person in the boat
                temp+=people[i]
            else: # one person already in the boat
                if temp+people[i]<=limit:
                    temp=0
                else:
                    temp=0
                    temp+=people[i]
                cnt+=1
        if temp!=0: cnt+=1
        return cnt



class tester(unittest.TestCase):
    def test1(self):
        people = [1,2]
        limit = 3
        Output= 1
        self.assertEqual(Output,Solution().numRescueBoats(people, limit))
    def test2(self):
        people = [3,2,2,1]
        limit = 3
        Output= 3
        self.assertEqual(Output,Solution().numRescueBoats(people, limit))
    def test3(self):
        people = [3,5,3,4]
        limit = 5
        Output= 4
        self.assertEqual(Output,Solution().numRescueBoats(people, limit))
    def test4(self):
        people = [5,1,4,2]
        limit = 6
        Output= 2
        self.assertEqual(Output,Solution().numRescueBoats(people, limit))