from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import *
def get_sol(): return Solution()
class Solution:
    def numberToWords(self, num: int) -> str:
        di={ 1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine', 10:'Ten',
             11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',18:'Eighteen',19:'Nineteen',20:'Twenty',
             30:'Thirty',40:'Forty',50:'Fifty',60:'Sixty',70:'Seventy',80:'Eighty',90:'Ninety',100:'Hundred',1000:'Thousand',10**6:'Million',10**9:'Billion'}
        def recur(s:str):
            s=str(int(s)) # remove leading zeros
            if s=='0': return '' # 0 has been dealt separately. So return empty string
            if int(s)<=20:
                return di[int(s)]

            n=len(s)
            res=[]
            if n==2:
                howManyTens=int(s[0]) # eg 40 has 4 tens. 30 has 3 tens
                res.append(di[howManyTens*10])
                res.append(recur(s[1:]))
                return ' '.join(res)
            if n==3:
                howManyHundreds=int(s[0])
                res.append(di[howManyHundreds])
                res.append(di[100])
                res.append(recur(s[1:]))
                return ' '.join(res)
            else:
                noOfDigitsAfterFirstComma=((n-1)//3)*3 # noOfDigitsAfterFirstComma will be 3,6,9 or 12
                # comma added for explanation. No comma exists in actual string
                # if s==    ' 6,543'  -> beforeFirstComma= 6  afterFirstComma=    543
                # if s=='98,765,432' ->  beforeFirstComma=98  afterFirstComma=765,432
                beforeFirstComma=recur(s[:-noOfDigitsAfterFirstComma])
                afterFirstComma =recur(s[-noOfDigitsAfterFirstComma:])
                res.append(beforeFirstComma)
                res.append(di[10**noOfDigitsAfterFirstComma])
                res.append(afterFirstComma)
                return ' '.join(res)


        if num==0: return 'Zero'
        res=recur(str(num))
        return ' '.join(res.split()) # remove double spaces

class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual("Twenty", get_sol().numberToWords(20))
    def test02(self):
        self.assertEqual("Thirteen", get_sol().numberToWords(13))
    def test03(self):
        self.assertEqual("Ten", get_sol().numberToWords(10))
    def test04(self):
        self.assertEqual("Twenty Three", get_sol().numberToWords(23))
    def test05(self):
        self.assertEqual("One Hundred Twenty Three", get_sol().numberToWords(123))
    def test06(self):
        self.assertEqual( "Twelve Thousand Three Hundred Forty Five", get_sol().numberToWords(12345))
    def test07(self):
        self.assertEqual("One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven", get_sol().numberToWords(1234567))
    def test08(self):
        self.assertEqual("Zero", get_sol().numberToWords(0))
    def test09(self):
        self.assertEqual("One Hundred", get_sol().numberToWords(100))
    def test10(self):
        self.assertEqual("One Thousand", get_sol().numberToWords(1000))
    def test11(self):
        self.assertEqual("One Thousand One", get_sol().numberToWords(1001))
