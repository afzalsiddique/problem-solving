import itertools; import math; import operator; import random; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce; from heapq import *; import unittest; from typing import List; import functools
from ..template.binary_tree import deserialize,serialize
def get_sol(): return Solution()
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self): return str(self.val)
class Solution:
    # tle
    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:
        g=defaultdict(dict)
        q=deque([root])
        while q:
            for _ in range(len(q)):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                    g[node.val][node.left.val]='L'
                    g[node.left.val][node.val]='U'
                if node.right:
                    q.append(node.right)
                    g[node.val][node.right.val]='R'
                    g[node.right.val][node.val]='U'

        q=deque([(startValue,"")])
        while q:
            for _ in range(len(q)):
                val,dir=q.popleft()
                if val==destValue: return dir
                for child in g[val]:
                    q.append((child,dir+g[val][child]))



class tester(unittest.TestCase):
    def test1(self):
        Output= "UURL"
        self.assertEqual(Output,get_sol().getDirections(deserialize("5,1,2,3,null,6,4"), startValue = 3, destValue = 6))
    def test2(self):
        Output= "L"
        self.assertEqual(Output,get_sol().getDirections(deserialize("2,1"), startValue = 2, destValue = 1))
    def test3(self):
        Output= "UUUUUUUUURRRLRLLRLL"
        self.assertEqual(Output,get_sol().getDirections(deserialize("29,6,212,191,331,335,161,211,228,null,128,80,314,332,352,null,223,267,21,null,null,344,null,353,49,48,194,103,269,1,null,65,null,315,250,300,27,3,347,147,274,121,317,360,281,231,324,311,215,149,244,85,325,225,175,58,40,156,95,2,45,null,null,null,null,263,237,320,null,341,351,null,null,334,null,66,18,207,227,277,null,292,355,31,null,354,33,265,261,318,140,132,50,260,null,null,null,94,46,251,307,358,152,275,4,179,171,44,41,282,326,177,158,104,181,null,null,298,null,256,289,357,null,null,99,364,329,78,null,229,70,157,102,123,230,null,null,null,115,118,248,null,253,294,55,null,32,null,null,null,null,null,null,204,154,null,76,184,234,180,79,319,null,209,null,37,109,null,11,null,null,330,153,137,338,206,null,185,245,295,243,316,106,38,144,145,64,null,134,null,null,null,163,142,280,null,null,null,null,null,null,361,null,54,69,120,293,284,288,92,null,221,150,322,72,null,null,63,62,null,283,101,327,56,null,131,null,null,null,null,null,null,null,null,null,null,null,null,359,null,186,126,null,57,188,null,null,null,null,null,null,89,null,151,null,null,null,164,null,356,null,135,232,null,51,310,null,252,291,null,34,null,297,null,321,71,166,110,182,309,266,91,169,null,null,null,null,null,null,205,203,167,null,null,217,192,12,null,136,176,122,148,116,88,7,208,null,328,98,97,226,162,null,77,null,null,247,255,301,258,null,339,null,null,15,349,null,53,313,null,143,null,null,238,null,null,null,null,264,87,null,254,141,337,null,36,null,null,null,null,null,null,null,195,null,259,216,null,null,null,null,null,111,null,114,null,null,null,null,220,333,null,262,52,193,222,8,null,null,null,365,null,93,null,35,343,null,null,null,345,30,null,null,276,272,null,null,199,5,null,197,null,null,219,75,210,null,323,342,10,290,null,null,178,null,null,null,336,null,17,null,130,190,90,139,96,null,257,null,null,null,127,22,174,350,null,null,null,null,null,null,null,null,null,null,86,null,null,null,null,235,25,null,null,null,null,null,null,null,82,366,24,null,null,14,null,null,168,null,112,13,240,null,67,108,null,null,105,117,null,null,null,172,198,null,26,340,null,null,null,39,null,null,362,null,107,23,233,84,241,296,null,null,129,308,null,null,null,null,null,278,273,173,249,363,299,302,null,null,null,null,null,null,null,304,null,201,null,213,null,20,null,null,null,null,null,null,null,59,null,187,null,null,null,null,146,null,160,null,124,null,100,null,null,28,133,null,159,73,null,null,null,null,null,null,null,236,165,43,60,312,null,null,null,null,null,null,null,null,null,null,19,null,null,null,null,null,null,null,null,null,null,null,null,null,285,null,246,61,null,null,null,202,null,183,200,null,null,196,305,348,214,null,null,null,null,null,null,null,null,null,null,null,null,null,287,null,null,83,null,null,null,218,null,null,null,null,null,null,null,null,null,346,74,null,null,null,279,null,null,null,null,119,null,null,null,null,null,null,null,null,null,null,null,null,189,null,81,239,9,224,null,null,null,null,null,null,null,null,null,null,null,null,286,170,null,null,null,303,306,null,null,null,42,68,null,113,270,null,null,125,null,null,47,268,null,null,null,16,null,null,271,null,null,155,null,null,null,null,null,138,null,null,null,null,null,null,null,null,242"), 131, 178))
    def test4(self):
        Output= "UUUUURRRLLLRLLRRR"
        self.assertEqual(Output,get_sol().getDirections(deserialize("5,3,327,246,245,194,54,112,51,66,31,345,299,237,268,154,1,11,44,136,78,110,7,null,279,73,219,284,114,227,203,261,33,null,256,334,63,null,189,97,null,166,72,300,168,264,263,238,296,null,null,213,229,250,4,175,176,294,108,177,332,305,null,null,null,null,null,36,180,291,143,95,35,23,215,233,349,14,275,351,null,null,335,99,346,98,141,328,45,null,235,338,255,null,null,null,null,220,null,null,null,10,318,159,178,47,319,147,134,null,313,null,null,186,231,130,199,null,null,163,116,86,253,null,null,257,58,102,56,9,70,24,222,113,135,145,null,100,null,null,77,221,null,348,21,329,210,285,null,null,129,322,null,null,306,183,null,149,null,106,null,null,null,null,null,137,336,53,244,326,null,311,302,null,239,null,90,151,null,2,61,304,127,94,43,null,null,266,null,165,105,104,null,null,320,200,57,16,138,null,null,null,316,34,null,169,85,310,269,68,323,350,202,null,126,119,62,211,223,42,140,null,null,206,null,120,160,null,null,null,124,150,324,null,null,null,null,74,null,174,null,null,null,182,null,265,null,null,null,207,277,96,196,25,28,null,null,340,171,null,null,null,null,null,347,267,null,null,32,191,192,179,null,295,null,195,null,181,null,null,null,null,null,115,null,null,309,49,325,258,190,null,null,224,null,null,337,225,184,null,48,null,null,null,null,20,280,209,161,null,null,null,null,38,281,339,null,230,71,null,null,303,101,null,null,null,null,null,317,91,null,193,null,null,13,null,null,344,132,89,93,null,null,null,314,null,null,null,null,330,19,123,331,null,null,null,null,null,null,22,null,null,271,null,null,55,null,292,290,248,null,null,null,null,null,251,67,null,null,273,null,260,null,307,null,69,131,81,167,214,343,null,243,null,283,null,null,null,null,null,216,111,null,null,18,204,148,null,null,null,12,315,87,146,null,185,188,null,null,null,321,null,null,null,15,217,301,null,null,null,null,null,218,null,null,null,142,287,46,null,null,341,64,29,null,259,27,298,null,75,null,156,null,null,null,null,null,null,null,null,null,null,288,125,null,242,139,82,270,null,null,null,152,null,null,null,null,40,null,null,null,226,null,null,198,null,null,null,null,103,122,null,278,null,null,null,null,164,274,null,null,null,76,37,8,286,null,232,null,null,155,null,null,null,30,null,null,null,null,null,null,null,null,276,197,null,50,342,null,6,null,65,null,null,null,null,null,247,null,null,null,null,null,null,null,null,null,null,201,39,null,null,null,null,109,null,null,null,null,null,121,84,79,null,null,null,null,282,null,null,293,null,null,333,297,234,null,null,null,null,null,null,null,null,52,133,null,null,null,172,null,252,null,17,170,59,158,236,null,null,null,162,262,null,null,null,107,null,null,308,null,null,null,null,249,352,null,null,null,null,157,null,null,60,null,null,null,null,null,null,254,212,83,null,null,240,173,153,null,208,128,272,null,null,187,205,null,null,null,null,null,null,null,null,null,null,null,null,144,null,312,null,null,88,41,null,null,null,null,null,null,289,null,null,null,null,null,null,null,null,null,null,null,null,92,null,228,117,null,80,118,null,null,null,241,26"), 223, 92))
    # def test5(self):
