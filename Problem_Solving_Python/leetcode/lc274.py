import random
from bisect import bisect_left
from collections import deque, defaultdict, Counter
from heapq import *
import unittest
from typing import List

# https://leetcode.com/problems/h-index/discuss/70768/Java-bucket-sort-O(n)-solution-with-detail-explanation
# counting sort
class Solution:
    def hIndex(self, citations):
        n = len(citations)
        buckets = [0 for _ in range(n + 1)]

        for num in citations:
            if num >= n:
                buckets[n] += 1
            else:
                buckets[num] += 1

        count = 0

        for i in reversed(range(len(buckets))):
            count += buckets[i]

            if count >= i:
                return i

        return 0
