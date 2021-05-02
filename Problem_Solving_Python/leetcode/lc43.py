import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List
import heapq



class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n, m = len(num1), len(num2)
        if not n or not m:
            return "0"

        result = [0] * (n + m)
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                current = int(result[i + j + 1]) + int(num1[i]) * int(num2[j])
                result[i + j + 1] = current % 10
                result[i + j] += current // 10

        for i, c in enumerate(result):
            if c != 0:
                return "".join(map(str, result[i:]))

        return "0"

class Solution2:
    def multiply(self, num1: str, num2: str) -> str:
        n1,n2=len(num1),len(num2)
        product=['0']*(n1+n2)
        for j in reversed(range(n2)):
            carry=0
            for i in reversed(range(n1)):
                temp1,temp2=int(num1[i]),int(num2[j])
                temp3=int(product[i+j+1])
                product[i+j+1]=str((temp1*temp2+temp3+carry)%10)
                carry=(temp1*temp2+temp3+carry)//10
            temp4=int(product[i+j])
            product[i+j]=str((temp4+carry)%10) # 99*99 will fail if removed
        i=0
        for i in range(n1+n2):
            if product[i]!='0':
                break
        return ''.join(product[i:])
class tester(unittest.TestCase):
    def test1(self):
        self.assertEqual('56088',Solution().multiply('123','456'))
    def test2(self):
        self.assertEqual('672',Solution().multiply('12','56'))
    def test3(self):
        self.assertEqual('891',Solution().multiply('9','99'))
    def test4(self):
        self.assertEqual("998001",Solution().multiply('999','999'))
    def test5(self):
        self.assertEqual("9801",Solution().multiply('99','99'))
    def test6(self):
        self.assertEqual("256",Solution().multiply('16','16'))
