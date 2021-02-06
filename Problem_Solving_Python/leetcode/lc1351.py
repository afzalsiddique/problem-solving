# https://www.youtube.com/watch?v=edJ19qIL8WQ
from bisect import bisect_left
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        summ=0
        for row in grid:
            summ+=bisect_left(row[::-1],0)
        return summ


# def search(li, key)->int:
#     return bisect_left(li, key)
#
# a = [11,10,9,8,7,6,5,4,3,3,3,3,3,3,2,1,1,1,0,0,0,-1,-2,-2,-3,-4,-15,-15,-15]
# print(search(a[::-1],0))