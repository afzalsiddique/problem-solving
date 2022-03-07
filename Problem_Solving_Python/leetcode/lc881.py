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
    def numRescueBoats(self, A: List[int], limit: int) -> int:
        def canCarry(noOfBoats):
            cnt=0
            i,j=0,n-1
            while i<j:
                if A[i]+A[j]<=limit:
                    i+=1
                    j-=1
                else:
                    j-=1
                cnt+=1
            if i==j:
                cnt+=1
            return cnt<=noOfBoats

        n=len(A)
        A.sort()
        lo,hi=0,n
        while lo<=hi:
            m=(lo+hi)//2
            if canCarry(m):
                hi=m-1
            else:
                lo=m+1
        return lo

class Solution3:
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
    def test01(self):
        self.assertEqual(1,get_sol().numRescueBoats([1,2], 3))
    def test02(self):
        self.assertEqual(3,get_sol().numRescueBoats([3,2,2,1], 3))
    def test03(self):
        self.assertEqual(4,get_sol().numRescueBoats([3,5,3,4], 5))
    def test04(self):
        self.assertEqual(2,get_sol().numRescueBoats([5,1,4,2], 6))