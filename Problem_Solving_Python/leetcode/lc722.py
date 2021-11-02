import functools; import itertools; import math; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import lru_cache, cache; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    # wrong
    def removeComments(self, source: List[str]) -> List[str]:
        n=len(source)
        res = []
        i=0
        while i<n:
            j=0
            tmp = []

            while j<len(source[i]):
                x = source[i][j]
                if j+1<len(source[i]) and source[i][j]=='/' and source[i][j+1]=='/':
                    break
                elif j+1<len(source[i]) and source[i][j]=='/' and source[i][j+1]=='*':
                    y = source[i][j]
                    while i<n and j<len(source[i]):
                        z = source[i][j]
                        if j+1<len(source[i]) and source[i][j]=='*' and source[i][j+1]=='/':
                            j+=1
                            break
                        j+=1
                        if j==len(source[i]):
                            i+=1
                            j=0
                else:
                    tmp.append(source[i][j])

                j+=1
            if ''.join(tmp):
                res.append(''.join(tmp))
            i+=1
        return res
class MyTestCase(unittest.TestCase):
    def test1(self):
        source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
        Output= ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]
        self.assertEqual(Output, get_sol().removeComments(source))
    def test2(self):
        source = ["a/*comment", "line", "more_comment*/b"]
        Output= ["ab"]
        self.assertEqual(Output, get_sol().removeComments(source))
    def test3(self):
        source = ["main() { ", "  int a = 1; /* Its comments here ", "", "  ", "  */ return 0;", "} "]
        Output= ["main() { ","  int a = 1;  return 0;","} "]
        self.assertEqual(Output, get_sol().removeComments(source))

    # def test4(self):
    # def test5(self):
