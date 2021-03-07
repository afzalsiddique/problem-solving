from typing import List


# class Solution:
#     def minElements(self, nums: List[int], limit: int, goal: int) -> int:
def minElements(nums: List[int], limit: int, goal: int) -> int:
    summ = sum(nums)
    remaining = summ-goal
    return abs(remaining//limit) if remaining%limit==0 else abs(remaining//limit) + 1

print(minElements([1], 3, -4), 0)
print(minElements([1], 3, -4), 0)
print(minElements([], 3, -4), 0)
print(minElements([2], 3, -4), 0)


print(minElements([1,-1,1], 3, -4), 2)
print(minElements([1,-10,9, 1], 100, 0), 1)
print(minElements([2,2,2,5,1,-2],5,126614243), 25322847)

