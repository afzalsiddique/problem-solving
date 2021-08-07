import itertools; import math; import operator; import random; import re; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from heapq import *; import unittest; from typing import List;
def get_sol(): return Solution()
class Solution:
    def entityParser(self, text: str) -> str:
        def find_entity(start):
            for ent in entities:
                if ent in text[start:start+len(ent)]:
                    return ent
            return None

        n=len(text)
        entities=["&quot;","&apos;","&amp;","&gt;","&lt;","&frasl;"]
        di={"&quot;":"\"","&apos;":"'","&amp;":"&","&gt;":">","&lt;":"<","&frasl;":"/"}
        res=[]
        i=0
        while i<n:
            ent=find_entity(i)
            if ent:
                res.append(di[ent])
                i+=len(ent)
            else:
                res.append(text[i])
                i+=1
        return ''.join(res)

class Tester(unittest.TestCase):
    def test_1(self):
        text = "&amp; is an HTML entity but &ambassador; is not."
        Output= "& is an HTML entity but &ambassador; is not."
        self.assertEqual(Output,get_sol().entityParser(text))
    def test_2(self):
        text = "and I quote: &quot;...&quot;"
        Output= "and I quote: \"...\""
        self.assertEqual(Output,get_sol().entityParser(text))
    def test_3(self):
        text = "Stay home! Practice on Leetcode :)"
        Output= "Stay home! Practice on Leetcode :)"
        self.assertEqual(Output,get_sol().entityParser(text))
    def test_4(self):
        text = "x &gt; y &amp;&amp; x &lt; y is always false"
        Output= "x > y && x < y is always false"
        self.assertEqual(Output,get_sol().entityParser(text))
    def test_5(self):
        text = "leetcode.com&frasl;problemset&frasl;all"
        Output= "leetcode.com/problemset/all"
        self.assertEqual(Output,get_sol().entityParser(text))
    # def test_6(self):
    # def test_7(self):
    # def test_8(self):