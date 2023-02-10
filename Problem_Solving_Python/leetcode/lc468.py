from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
class Solution:
    def ip_v4(self,s:str):
        for c in s:
            if c=='.' or '0'<=c<='9': continue
            return False
        li=s.split('.')
        if len(li)!=4:
            return False
        if any(x=='' for x in li):
            return False
        if any(x[0]=='0' for x in li if len(x)!=1):
            return False
        return all(0<=int(x)<=255 for x in li)
    def ip_v6(self,s:str):
        for c in s:
            if c==':' or '0'<=c<='9' or 'A'<=c<='F' or 'a'<=c<='f': continue
            return False
        li=s.split(':')
        if len(li)!=8: return False
        if any(not 1<=len(x)<=4 for x in li):
            return False
        return True
    def validIPAddress(self, queryIP: str) -> str:
        if self.ip_v4(queryIP):
            return "IPv4"
        if self.ip_v6(queryIP):
            return "IPv6"
        return "Neither"
class Solution2:
    def ip_v4(self, ip):
        ip = ip.split('.')
        if len(ip)!=4: return False
        for x in ip:
            if not self.valid_v4_helper(x): return False
        return True
    def valid_v4_helper(self, x):
        if len(x)==0 or len(x)>3: return False
        if len(x)>1: # 01 is invalid
            valid = (0 < ord(x[0]) - ord('0') <= 9)
            if not valid: return False
        for i in range(len(x)):
            valid = (0 <= ord(x[i]) - ord('0') <= 9)
            if not valid: return False
        if int(x)<0 or int(x)>255: return False
        return True
    def ip_v6(self, ip):
        ip = ip.split(':')
        if len(ip)!=8: return False
        for x in ip:
            if not self.valid_v6_helper(x): return False
        return True
    def valid_v6_helper(self, x):
        if len(x)==0 or len(x)>4: return False
        for i in range(len(x)):
            valid = (0 <= ord(x[i]) - ord('0') <= 9) or \
                    (0 <= ord(x[i]) - ord('a') <= 5) or \
                    (0 <= ord(x[i]) - ord('A') <= 5)
            if not valid: return False
        return True
    def validIPAddress(self, ip: str) -> str:
        if self.ip_v4(ip):
            return 'IPv4'
        elif self.ip_v6(ip):
            return 'IPv6'
        return 'Neither'




class Tester(unittest.TestCase):
    def test01(self):
        self.assertEqual("IPv4",get_sol().validIPAddress("172.16.254.1"))
    def test02(self):
        self.assertEqual("Neither",get_sol().validIPAddress("@1.16.254.1"))
    def test03(self):
        self.assertEqual("Neither",get_sol().validIPAddress("1@.16.254.1"))
    def test04(self):
        self.assertEqual("Neither",get_sol().validIPAddress("12.16.256.1"))
    def test05(self):
        self.assertEqual("IPv6",get_sol().validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
    def test06(self):
        self.assertEqual("IPv4",get_sol().validIPAddress("172.16.254.1"))
    def test07(self):
        self.assertEqual("IPv6",get_sol().validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
    def test08(self):
        self.assertEqual("Neither",get_sol().validIPAddress("256.256.256.256"))
    def test09(self):
        self.assertEqual("Neither",get_sol().validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334:"))
    def test10(self):
        self.assertEqual("Neither",get_sol().validIPAddress("1e1.4.5.6"))
    def test11(self):
        self.assertEqual("IPv4",get_sol().validIPAddress("192.0.0.1"))
    def test12(self):
        self.assertEqual("Neither",get_sol().validIPAddress("1.0.1."))
    def test13(self):
        self.assertEqual("Neither",get_sol().validIPAddress("00.0.1.0"))
