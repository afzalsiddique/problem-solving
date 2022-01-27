from itertools import accumulate; from math import floor,ceil; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce,cache; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt; from sortedcontainers import SortedList
from binary_tree_tester import *
def get_sol(): return Solution()
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def getSum(left,right): return pre[right+1]-pre[left] # both inclusive
        def justify(li:List[str],noOfSpaces:int):
            noOfGaps = len(li)-1
            extraSpaces=noOfSpaces%noOfGaps # number of extra spaces after equally dividing
            ans=[]

            ans.append(li[0])
            for i in range(1,len(li)):
                gap=noOfSpaces//noOfGaps
                gap+=1 if i<=extraSpaces else 0 # If the number of spaces does not divide evenly between words, the empty slots on the left will be assigned more spaces
                ans.append(' '*gap)
                ans.append(li[i])
            return ''.join(ans)
        def justifyLeft(li:List[str]):
            tmp=' '.join(li)
            return tmp + ' '*(maxWidth-len(tmp))

        n=len(words)
        pre=[len(w) for w in words] # presum
        pre=[0]+list(accumulate(pre)) # presum

        i,j=0,-1 # i,j both inclusive
        res=[]
        while i<n:
            while j+1<n:
                newJ=j+1
                tmp= getSum(i,newJ)+(newJ-i)
                if tmp<=maxWidth:
                    j+=1
                else:
                    break
            # while j+1<n and getSum(i,j+1)+(j+1-i)<=maxWidth: # could be simplified
            #     j+=1
            x = [words[idx] for idx in range(i,j+1)]
            noOfSpaces = maxWidth-getSum(i,j)
            if j==n-1 or len(x)==1: # last line and when there is only one word
                res.append(justifyLeft(x))
            else:
                res.append(justify(x,noOfSpaces))
            i=j+1
        return res



class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual([ "This    is    an", "example  of text", "justification.  " ], get_sol().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
    def test02(self):
        self.assertEqual([ "What   must   be", "acknowledgment  ", "shall be        " ], get_sol().fullJustify(["What","must","be","acknowledgment","shall","be"], 16))
    def test03(self):
        self.assertEqual([ "Science  is  what we", "understand      well", "enough to explain to", "a  computer.  Art is", "everything  else  we", "do                  " ], get_sol().fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20))
    # def test04(self):
    # def test05(self):
    # def test06(self):
    # def test07(self):
    # def test08(self):
    # def test09(self):
    # def test10(self):
