from itertools import accumulate; from math import floor,ceil,sqrt; import operator; import random; import string; from bisect import *; from collections import deque, defaultdict, Counter, OrderedDict; from functools import reduce, cache, total_ordering; from heapq import *; import unittest; from typing import List,Optional; from functools import cache; from operator import lt, gt
from binary_tree_tester import ser,des; from a_linked_list import make_linked_list
def get_sol(): return Solution()
@total_ordering
class Element:
    def __init__(self, count, word):
        self.count = count
        self.word = word
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.idx
        return self.count < other.count
    def __eq__(self, other): return self.count == other.count and self.word == other.idx

class Solution:
    # heap
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        freqs = []
        heapify(freqs)
        for word, count in counts.items():
            heappush(freqs, (Element(count, word), word))
            if len(freqs) > k:
                heappop(freqs)

        res = []
        for _ in range(k):
            res.append(heappop(freqs)[1])
        return res[::-1]

class Solution2:
    # buckets
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count=Counter(words)
        maxx=max(count.values())
        buckets=[[] for _ in range(maxx+1)]
        for word in count:
            buckets[count[word]].append(word)
        for li in buckets:
            li.sort(reverse=True)

        res=[]
        i=maxx
        while k:
            j=len(buckets[i])-1
            tmp=[]
            while k and j>=0:
                tmp.append(buckets[i][j])
                j-=1
                k-=1
            res.extend(tmp)
            i-=1
        return res
class MyTestCase(unittest.TestCase):
    def test01(self):
        self.assertEqual(["i", "love"], get_sol().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"],  2))
    def test02(self):
        self.assertEqual(["the", "is", "sunny", "day"], get_sol().topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))
    def test03(self):
        self.assertEqual(["i"], get_sol().topKFrequent(["i","love","leetcode","i","love","coding"], 1))
