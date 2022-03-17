from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
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
class Solution3:
    def multiply(self, num1: str, num2: str) -> str:
        def add(li1:List[int],li2:List[int]):
            n=max(len(li1),len(li2))
            li1=[0]*(n-len(li1)+1)+li1
            li2=[0]*(n-len(li2)+1)+li2
            res=[]
            carry=0
            while li1 and li2:
                tmp=li1.pop()+li2.pop()+carry
                carry=tmp//10
                tmp=tmp%10
                res.append(tmp)
            res.reverse()
            return res

        def oneDigitMul(s:str, digit:str, zeros):
            digit=int(digit)
            carry=0
            res=[]
            for d in map(int,s[::-1]):
                tmp= d * digit + carry
                carry=tmp//10
                tmp=tmp%10
                res.append(tmp)
            while carry:
                res.append(carry%10)
                carry//=10
            res.reverse()
            res.extend([0 for _ in range(zeros)])
            return res

        res=[]
        for i,digit in enumerate(num2[::-1]):
            zeros=i
            tmp=oneDigitMul(num1,digit,zeros)
            res=add(res,tmp)

        i=0 # remove leading zeros
        while i<len(res) and res[i]==0:
            i+=1
        res=res[i:]
        if not res: res=[0]
        return ''.join(map(str,res))
class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual('56088',get_sol().multiply('123','456'))
    def test02(self):
        self.assertEqual('672',get_sol().multiply('12','56'))
    def test03(self):
        self.assertEqual('891',get_sol().multiply('9','99'))
    def test04(self):
        self.assertEqual("998001",get_sol().multiply('999','999'))
    def test05(self):
        self.assertEqual("9801",get_sol().multiply('99','99'))
    def test06(self):
        self.assertEqual("256",get_sol().multiply('16','16'))
    def test07(self):
        self.assertEqual("0",get_sol().multiply("9133", "0"))
    def test08(self):
        self.assertEqual("114",get_sol().multiply("3", "38"))
