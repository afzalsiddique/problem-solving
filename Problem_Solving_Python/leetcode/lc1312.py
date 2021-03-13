# https://www.youtube.com/watch?v=DOnK40BvazI&t=300s
################# SAME AS LONGEST COMMON SUBSEQUENCE ##########
################ SAME AS LONGEST PALINDROMIC SUBSEQUENCE ###########
import unittest
from typing import List

class Solution:
    def minInsertions(self, s: str) -> int:
        di = {}
        def helper(s):
            n = len(s)
            if n==0 or n==1:return 0
            if n==2:
                if s[0]==s[1]:return 0
                else: return 1
            if s in di:return di[s]
            if s[0]==s[-1]:
                di[s] = helper(s[1:-1]) # remove one char from both ends
                return di[s]
            else:
                di[s]= 1+min(helper(s[:-1]), helper(s[1:]))
                return di[s]

        return helper(s)



class MyTestCase(unittest.TestCase):

    def test_1(self):
        a =Solution().minInsertions('zzazz')
        e = 0
        self.assertEqual(e, a)


    def test_2(self):
        a =Solution().minInsertions( "mbadm" )
        e = 2
        self.assertEqual(e, a)

    def test_3(self):
        a =Solution().minInsertions( "leetcode" )
        e = 5
        self.assertEqual(e, a)
