# https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76583/11ms-JAVA-solution-using-merge-sort-with-explanation
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def mergesort(nums, index, l, r, res):
            if l >= r:
                return
            mid = (l + r) // 2
            mergesort(nums, index, l, mid, res)
            mergesort(nums, index, mid + 1, r, res)
            merge(nums, index, l, mid, mid + 1, r, res)

        def merge(nums, index, f_left, f_right, s_left, s_right, res):
            start = f_left
            tmp = [0] * (s_right - f_left + 1)
            right_count = 0
            p = 0
            while f_left <= f_right and s_left <= s_right:
                if nums[index[f_left]] > nums[index[s_left]]:
                    tmp[p] = index[s_left]
                    p += 1
                    s_left += 1
                    right_count += 1
                else:
                    res[index[f_left]] += right_count
                    tmp[p] = index[f_left]
                    p += 1
                    f_left += 1
                if f_left > f_right:
                    tmp[p] = index[s_left]
                    p += 1
                    s_left += 1
                elif s_left > s_right:
                    res[index[f_left]] += right_count
                    tmp[p] = index[f_left]
                    p += 1
                    f_left += 1
            for i in range(len(tmp)):
                index[start + i] = tmp[i]

        res = [0] * len(nums)
        index = [0] * len(res)
        for i in range(len(res)):
            index[i] = i
        mergesort(nums, index, 0, len(nums) - 1, res)
        li = []
        for i in res:
            li.append(i)
        return li

# # https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76583/11ms-JAVA-solution-using-merge-sort-with-explanation
# from typing import List
#
# class Solution:
#     def countSmaller(self, nums: List[int]) -> List[int]:
#         def mergesort(nums, indexes, start, end, count):
#             if end<=start:
#                 return
#             mid = (start + end) //2
#             mergesort(nums, indexes, start, mid, count)
#             mergesort(nums, indexes, mid + 1, end, count)
#             merge(nums, indexes, start, end, count)
#         def merge(nums, indexes, start, end, count):
#             mid = (start + end) // 2
#             left_index = start
#             right_index = mid + 1
#             rightcount = 0
#             new_indexes = [0] * (end-start+1)
#
#             sort_index = 0
#             while left_index <= mid and right_index <= end:
#                 if nums[indexes[right_index]] < nums[indexes[left_index]]:
#                     new_indexes[sort_index] = indexes[right_index]
#                     rightcount+=1
#                     right_index+=1
#                 else:
#                     new_indexes[sort_index] = indexes[left_index]
#                     count[indexes[left_index]] += rightcount
#                     left_index+=1
#                 sort_index+=1
#             while left_index <=mid:
#                 new_indexes[sort_index] = indexes[left_index]
#                 count[indexes[left_index]] += rightcount
#                 left_index+=1
#                 sort_index+=1
#             while right_index <= end:
#                 new_indexes[sort_index] = indexes[right_index]
#                 right_index+=1
#                 sort_index+=1
#             for i in range(start, end):
#                 indexes[i] = new_indexes[i-start]
#
#         res = []
#         count = [0] * len(nums)
#         indexes = [i for i in range(len(nums))]
#         mergesort(nums, indexes, 0, len(nums)-1, count)
#         for i in range(len(nums)):
#             res.append(count[i])
#         return res
