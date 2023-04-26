import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
# from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class Solution:
    # https://leetcode.com/problems/largest-multiple-of-three/discuss/518830/C%2B%2BJava-Concise-O(n)
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        d1=[1,4,7,2,5,8]
        d2=[2,5,8,1,4,7]
        count=Counter(digits)
        summ=sum(digits)
        while summ%3!=0:
            for d in d1 if summ%3==1 else d2:
                if count[d]:
                    summ-=d
                    count[d]-=1
                    break

        res=[]
        for i in range(9,-1,-1):
            while count[i]:
                res.append(str(i))
                count[i]-=1
        if not res:
            return ''
        if res[0]=='0':
            return '0'
        return ''.join(res)


class Solution2:
    def convert(self,digits):
        res= ''.join(map(str,digits))
        if res and res[0]=='0': # '00'
            return '0'
        return res
    def removeOneElement(self,mod,digits): # digits sorted in descending order
        for x in reversed(digits):
            if x%3==mod:
                return x
        return None
    def removeTwoElements(self,mod,digits): # digits sorted in descending order
        li = []
        for x in reversed(digits):
            if x%3==mod:
                li.append(x)
            if len(li)==2:
                break
        if len(li)==2:
            return li
        return None
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        digits.sort(reverse=True)
        summ=sum(digits)
        mod=summ%3
        if mod==0:
            return self.convert(digits)

        # remove one digit
        toBeRemoved=self.removeOneElement(mod,digits)
        if toBeRemoved is not None:
            digits.remove(toBeRemoved)
            return self.convert(digits)


        # REMOVE TWO DIGITS CAN BE GENERALIZED
        # toBeRemoved=self.removeTwoElements((mod+mod)%3,digits) # (2+2)%3=1 and (1+1)%3=2
        # if toBeRemoved is not None:
        #     for x in toBeRemoved:
        #         digits.remove(x)
        #     return self.convert(digits)
        # return ''

        # remove two digits
        if mod==1:
            toBeRemoved=self.removeTwoElements(2,digits) # (2+2)%3=1
            if toBeRemoved is not None:
                for x in toBeRemoved:
                    digits.remove(x)
                return self.convert(digits)
            return ''

        # if mod==2:
        toBeRemoved=self.removeTwoElements(1,digits) # (1+1)%3=2
        if toBeRemoved is not None:
            for x in toBeRemoved:
                digits.remove(x)
            return self.convert(digits)
        return ''

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual('981', get_sol().largestMultipleOfThree([8,1,9]))
    def test2(self):
        self.assertEqual('8760', get_sol().largestMultipleOfThree([8,6,7,1,0]))
    def test3(self):
        self.assertEqual('', get_sol().largestMultipleOfThree([1]))
    def test4(self):
        self.assertEqual('0', get_sol().largestMultipleOfThree([0,0,0,0,0,0]))
    def test5(self):
        self.assertEqual('111', get_sol().largestMultipleOfThree([1,1,1]))
    def test6(self):
        self.assertEqual('', get_sol().largestMultipleOfThree([5,8]))
    def test7(self):
        self.assertEqual('966', get_sol().largestMultipleOfThree([9,8,6,8,6]))
    def test8(self):
        self.assertEqual('966', get_sol().largestMultipleOfThree([9,7,6,7,6]))
    def test9(self):
        self.assertEqual('111', get_sol().largestMultipleOfThree([1,1,1,2]))
    def test10(self):
        self.assertEqual('99999999999999999999999999999999999999999999999999999988888888888888888888888888888888888888888888888888888888877777777777777777777777777777777777777777777777777666666666666666666666666666666666666666666666666666666666555555555555555555555555555555555555555555555555554444444444444444444444444444444444444444444443333333333333333333333333333333333333333333333333333333332222222222222222222222222222222222222222222222221111111111111111111111111111111111111111111111110000000000000000000000000000000000', get_sol().largestMultipleOfThree([6,0,8,2,6,3,5,8,6,3,0,9,8,0,8,5,4,5,1,6,9,3,0,4,7,4,3,7,8,2,6,8,3,3,7,9,2,6,6,9,9,7,8,3,5,9,8,1,1,2,9,8,8,3,8,1,9,5,3,1,7,2,0,0,4,5,0,1,3,5,8,8,4,4,0,7,5,2,4,3,6,7,5,8,6,6,8,3,4,1,3,9,0,7,3,1,1,9,3,7,2,6,7,6,4,5,6,1,5,0,6,0,6,0,7,4,6,4,2,6,3,1,4,6,8,6,0,2,1,8,5,2,9,7,9,6,3,2,2,9,3,7,1,9,7,3,3,7,6,4,6,1,8,8,5,6,6,8,7,1,5,0,7,2,2,9,4,0,7,5,3,5,8,1,1,5,8,8,2,4,1,6,8,0,5,5,7,0,2,8,9,9,9,3,8,3,2,2,9,3,1,1,7,3,2,3,9,6,6,1,3,7,4,7,6,7,5,4,5,0,7,7,4,9,5,8,5,6,1,6,1,6,9,9,3,4,4,8,6,7,1,8,2,7,7,4,3,9,7,9,4,8,3,6,2,0,2,1,3,8,7,7,6,4,8,3,6,9,8,1,3,3,6,3,6,8,5,3,4,8,3,3,5,3,8,7,0,1,9,1,2,1,2,9,9,9,2,1,5,6,4,4,9,3,1,0,3,0,0,5,8,5,5,4,6,6,5,4,7,4,1,4,7,0,7,1,6,4,5,0,8,2,9,3,1,7,7,9,9,2,5,6,6,8,2,9,5,8,4,5,6,3,5,2,7,7,2,1,3,2,2,7,9,8,7,7,4,4,5,1,6,1,8,9,3,0,4,6,3,5,4,1,0,8,9,6,9,8,0,2,9,1,6,7,1,0,8,7,5,4,0,5,6,9,5,7,1,5,2,1,5,9,2,5,6,9,8,9,3,7,3,3,6,5,9,3,8,2,9,4,6,9,5,7,8,0,6,3,4,5,8,6,4,1,8,8,9,3,2,0,4,2,1,9,6,7,7,2,9,2,8,2,6,2,1,3,8,5,1,6,2,0,7,2,8,1,0,2,2,5,9,5,8,2,5,1,2,3,9,4,8,9,8,9,3,4,3,4,4,3]))
    def test11(self):
        self.assertEqual('7770', get_sol().largestMultipleOfThree([8,7,0,7,7]))
