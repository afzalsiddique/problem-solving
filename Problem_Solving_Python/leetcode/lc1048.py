import unittest
from collections import deque
from typing import List
def get_sol_obj(): return Solution()


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        di={}
        sett={word for word in words}
        def helper(word):
            if not word: return 0
            if len(word)==1:
                if word in sett: return 1
                return 0
            if word not in sett: return 0
            if word in di: return di[word]
            ans=0
            for i in range(len(word)):
                ans = max(ans, 1+helper(word[:i]+word[i+1:]))
            di[word]=ans
            return di[word]
        maxx=0
        for word in words:
            maxx=max(maxx,helper(word))
        return maxx


class MyTestCase(unittest.TestCase):
    def test_01(self):
        words = ["a","b","ba","bca","bda","bdca"]
        Output= 4
        self.assertEqual(Output, get_sol_obj().longestStrChain(words))
    def test_02(self):
        words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
        Output= 5
        self.assertEqual(Output, get_sol_obj().longestStrChain(words))
