# https://www.youtube.com/watch?v=zaM_GLLvysw
from heapq import *
import unittest
from collections import Counter
from typing import List
class Solution(object):
    def reorganizeString(self, S):
        n = len(S)
        counter = Counter(S)
        pq = []
        res = []
        for letter in counter:
            pq.append((-counter[letter], letter))

        for count in counter.values():
            if count>(n+1)//2:
                return ""
        heapify(pq)
        while len(pq)>1:
            current = heappop(pq)
            curr_cnt, curr_char = current[0]*(-1), current[1] # -1 for min heap
            next = heappop(pq)
            next_cnt, next_char = next[0]*(-1), next[1] # -1 for min heap
            res.append(curr_char)
            res.append(next_char)
            curr_cnt-=1
            next_cnt -=1
            if curr_cnt>0: # - for min heap
                heappush(pq, (-curr_cnt, curr_char)) # - for min heap
            if next_cnt>0:
                heappush(pq, (-next_cnt, next_char))
        if pq:
            lastcount, lastchar = heappop(pq)
            if -(lastcount)>1:
                return ""
            res.append(lastchar)
        return "".join(res)

class MyTestCase(unittest.TestCase):

    def test_1(self):
        sol = Solution()
        actual = sol.reorganizeString("aab")
        expected = "aba"
        self.assertEqual(expected, actual)

    def test_2(self):
        sol = Solution()
        actual = sol.reorganizeString("aaab")
        expected = ""
        self.assertEqual(expected, actual)

    def test_3(self):
        sol = Solution()
        actual = sol.reorganizeString("vvvlo")
        expected = "vlvov"
        self.assertEqual(expected, actual)

    def test_4(self):
        sol = Solution()
        actual = sol.reorganizeString(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_5(self):
        sol = Solution()
        actual = sol.reorganizeString(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_6(self):
        sol = Solution()
        actual = sol.reorganizeString(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_7(self):
        sol = Solution()
        actual = sol.reorganizeString(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_8(self):
        sol = Solution()
        actual = sol.reorganizeString(0)
        expected = 0
        self.assertEqual(expected, actual)

    def test_9(self):
        sol = Solution()
        actual = sol.reorganizeString(0)
        expected = 0
        self.assertEqual(expected, actual)