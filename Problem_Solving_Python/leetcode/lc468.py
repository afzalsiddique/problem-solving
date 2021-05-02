import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List

class Solution:
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



class tester(unittest.TestCase):
    def test1(self):
        ip = "172.16.254.1"
        self.assertEqual(True,Solution().ip_v4(ip))
    def test2(self):
        ip = "@1.16.254.1"
        self.assertEqual(False,Solution().ip_v4(ip))
    def test3(self):
        ip = "1@.16.254.1"
        self.assertEqual(False,Solution().ip_v4(ip))
    def test4(self):
        ip = "12.16.256.1"
        self.assertEqual(False,Solution().ip_v4(ip))
    def test5(self):
        ip = "2001:0db8:85a3:0:0:8A2E:0370:7334"
        self.assertEqual(True,Solution().ip_v6(ip))
    def test6(self):
        IP = "172.16.254.1"
        Output= "IPv4"
        self.assertEqual(Output,Solution().validIPAddress(IP))
    def test7(self):
        IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
        Output= "IPv6"
        self.assertEqual(Output,Solution().validIPAddress(IP))
    def test8(self):
        IP = "256.256.256.256"
        Output= "Neither"
        self.assertEqual(Output,Solution().validIPAddress(IP))
    def test9(self):
        IP = "2001:0db8:85a3:0:0:8A2E:0370:7334:"
        Output= "Neither"
        self.assertEqual(Output,Solution().validIPAddress(IP))
    def test10(self):
        IP = "1e1.4.5.6"
        Output= "Neither"
        self.assertEqual(Output,Solution().validIPAddress(IP))
    def test11(self):
        IP = "192.0.0.1"
        Output= "IPv4"
        self.assertEqual(Output,Solution().validIPAddress(IP))
