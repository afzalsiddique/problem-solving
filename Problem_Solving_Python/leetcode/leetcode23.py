# Definition for singly-linked list.
from typing import List


class Solution:
    def mergeKLists(self, lists):
        n = len(lists)
        if n==1:
            return lists[0]

        mid = n//2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        merged_list = []

        i, j = 0, 0
        while True:
            if left[i]<right[j]:
                merged_list.append(left[i])
                i+=1
            else:
                merged_list.append(right[j])
                j+=1
            if i == len(left): # if end of left list is reached, merge the rest of right list
                while j != len(right):
                    merged_list.append(right[j])
                    j+=1
                break
            if j == len(right):
                while i!=len(left):
                    merged_list.append(left[i])
                    i+=1
                break
        return merged_list

