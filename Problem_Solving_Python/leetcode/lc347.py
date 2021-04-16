from heapq import *
import unittest
from collections import Counter, defaultdict
import random

from typing import List


# bucket. Time: O(n)
# https://www.youtube.com/watch?v=EYFcQRwcqk0&t=133s
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        di,n= defaultdict(int), len(nums)
        bucket = [[] for _ in range(n+1)]
        for num in nums:
            di[num]+=1
        for num in di:
            bucket[di[num]].append(num)
        res = []
        for i in reversed(range(n+1)):
            if not bucket[i]:continue
            for item in bucket[i]:
                if k==0:return res
                res.append(item)
                k-=1

        return res
# heap
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = []
        di = defaultdict(int)
        for num in nums:
            di[num]+=1

        for num in di:
            if len(pq)<k:
                heappush(pq,(di[num],num))
            else:
                lowest_freq,x = pq[0]
                if di[num]>lowest_freq:
                    heappop(pq)
                    heappush(pq,(di[num],num))
        res = [x[1] for x in pq]
        return res

# quick select
class Solution3:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        unique = list(count.keys())

        def partition(left, right, pivot_index) -> int:
            pivot_frequency = count[unique[pivot_index]]
            # 1. move pivot to end
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

            # 2. move all less frequent elements to the left
            i = left - 1
            for j in range(left, right):
                if count[unique[j]] < pivot_frequency:
                    i += 1
                    unique[i], unique[j] = unique[j], unique[i]

            # 3. move pivot to its final place
            unique[right], unique[i+1] = unique[i+1], unique[right]

            return i + 1

        def quickselect(left, right, k_smallest) -> None:
            """
            Sort a list within left..right till kth less frequent element
            takes its place.
            """
            # base case: the list contains only one element
            if left == right:
                return

            # select a random pivot_index
            pivot_index = random.randint(left, right)

            # find the pivot position in a sorted list
            pivot_index = partition(left, right, pivot_index)

            # if the pivot is in its final sorted position
            if k_smallest == pivot_index:
                return
                # go left
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)
            # go right
            else:
                quickselect(pivot_index + 1, right, k_smallest)

        n = len(unique)
        # kth top frequent element is (n - k)th less frequent.
        # Do a partial sort: from less frequent to the most frequent, till
        # (n - k)th less frequent element takes its place (n - k) in a sorted array.
        # All element on the left are less frequent.
        # All the elements on the right are more frequent.
        quickselect(0, n - 1, n - k)
        # Return top k frequent elements
        return unique[n - k:]


class mycase(unittest.TestCase):
    def test1(self):
        self.assertEqual([1,2],Solution().topKFrequent(nums = [1,1,1,2,2,3], k = 2))
