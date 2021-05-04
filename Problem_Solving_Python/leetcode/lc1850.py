import unittest
from collections import deque, defaultdict
from heapq import *
from typing import List
def get_sol_obj(): return Solution()

class Solution:
    # https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/discuss/1186823/Python-3-brute-force
    def getMinSwaps(self, num: str, k: int) -> int:
        def nxt_perm(num: list) -> list:
            i = n - 1
            while i > 0 and num[i-1] >= num[i]:
                i -= 1
            j = i
            while j < n and num[i-1] < num[j]:
                j += 1
            num[i-1], num[j-1] = num[j-1], num[i-1]
            num[i:] = num[i:][::-1] # credit to @ye15, reduce time from nlogn to n
            return num

        n = len(num)
        nxt_k_num = list(num)
        for _ in range(k):
            nxt_k_num = nxt_perm(nxt_k_num)

        ans = 0
        num = list(num)
        for i in range(n):
            j = i
            while j < n and nxt_k_num[i] != num[j]:
                j += 1
            ans += j - i
            num[i:j+1] = [num[j]] + num[i:j]
        return ans

