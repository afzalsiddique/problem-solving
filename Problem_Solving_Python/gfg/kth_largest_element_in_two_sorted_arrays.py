import math
import unittest
# https://yao.page/posts/kth-smallest-element-in-two-sorted-arrays-python/
# https://www.youtube.com/watch?v=LPFhl65R7ww&t=597s
class Solution:
    def kthElement(self,A, B,n,m, k):

        lo=0
        hi = len(A) # it's "len(A)" and not "len(A)-1". the maximum number that can be chosen from the first array

        # more efficient
        # If *all* elements in B are in B's left ptn,
        # we'll need at least k - len(B) elements
        # in A's left ptn
        # lo = max(0, k - len(B))

        # If k is less than the size of A, then we
        # only need at most k elements in A's left ptn
        # hi = min(len(A), k)

        def get_val(arr, i): # more detail: check out the link -> https://yao.page/posts/kth-smallest-element-in-two-sorted-arrays-python/
            if 0 <= i <= len(arr) - 1:
                return arr[i]
            return math.inf * (-1 if i < 0 else 1)

        while lo <= hi:
            A_size = (lo + hi) // 2 # A_size indicates left size of A
            B_size = k - A_size

            A_left, A_right = get_val(A, A_size-1), get_val(A, A_size)
            B_left, B_right = get_val(B, B_size-1), get_val(B, B_size)

            if A_left <= B_right and B_left <= A_right:
                return max(A_left, B_left)

            elif A_left > B_right:
                hi =A_size - 1

            else:  # B_left > A_right
                lo = A_size + 1




class MyTestCase(unittest.TestCase):
    def test_1(self):
        x = [1,3,5,7,9,11]
        y = [2,4,6,8,10]
        k = 6
        actual = Solution().kthElement(x,y,len(x),len(y), k)
        expected = 6
        self.assertEqual(expected, actual)








##############################################################################
# I've implemented kth Largest element. Geeksforgeeks question wants the kth smallest


class Solution:
    def kthElement(self, nums1, nums2,n,m, k):
        if len(nums1)>len(nums2):return self.kthElement(nums2, nums1,n,m, k)
        n1,n2= len(nums1), len(nums2)
        low,high=0,n1
        while low<=high:
            tmp = n1 + n2 - k
            partition_x = (low+high)//2
            partition_y = tmp - partition_x
            maxLeft_x = nums1[partition_x-1] if partition_x!=0 else float('-inf')
            minRight_x = nums1[partition_x] if partition_x!=n1 else float('inf')

            maxLeft_y = nums2[partition_y-1] if partition_y!=0 else float('-inf')
            minRight_y = nums2[partition_y] if partition_y!=n2 else float('inf')

            if maxLeft_x <= minRight_y and maxLeft_y<=minRight_x:
                return min(minRight_y, minRight_x)
            elif maxLeft_x>minRight_y:
                high = partition_x-1
            else:
                low=partition_x+1

# sol = Solution()
# x = [0,1,2,5,9]
# y = [-2,-1,3,4,6,8]
# k = 4
# print(sol.kthElement(x, y,len(x),len(y), k), 5)
# x = [1,10,10,25,40,54,79]
# y = [15, 24, 27, 32, 33, 39, 48, 68, 82, 88, 90]
# k = 15
# print(sol.kthElement(x, y,len(x),len(y), k), 15)









# https://yao.page/posts/kth-smallest-element-in-two-sorted-arrays-python/
def find_kth_smallest(A, B, k):

    lo=0
    hi = len(A) # it's "len(A)" and not "len(A)-1". the maximum number that can be chosen from the first array

    # more efficient
    # If *all* elements in B are in B's left ptn,
    # we'll need at least k - len(B) elements
    # in A's left ptn
    # lo = max(0, k - len(B))

    # If k is less than the size of A, then we
    # only need at most k elements in A's left ptn
    # hi = min(len(A), k)

    def get_val(arr, i): # more detail: check out the link -> https://yao.page/posts/kth-smallest-element-in-two-sorted-arrays-python/
        if 0 <= i <= len(arr) - 1:
            return arr[i]
        return math.inf * (-1 if i < 0 else 1)

    while lo <= hi:
        A_size = (lo + hi) // 2 # A_size indicates left size of A
        B_size = k - A_size

        A_left, A_right = get_val(A, A_size-1), get_val(A, A_size)
        B_left, B_right = get_val(B, B_size-1), get_val(B, B_size)

        if A_left <= B_right and B_left <= A_right:
            return max(A_left, B_left)

        elif A_left > B_right:
            hi =A_size - 1

        else:  # B_left > A_right
            lo = A_size + 1




class MyTestCase2(unittest.TestCase):
    def test_3(self):
        x = [1,3,5,7,9,11]
        y = [2,4,6,8,10]
        k = 6
        actual = find_kth_smallest(x,y, k)
        expected = 5
        self.assertEqual(expected, actual)






# Base cases:
#
# If length of one of the arrays is 0, the answer is kth element of the second array.
# Reduction steps:
#
# If mid index of a + mid index of b is less than k:
# If mid element of a is greater than mid element of b, we can ignore the first half of b, adjust k.
# Otherwise, ignore the first half of a, adjust k.
# If k is less than sum of mid indices of a and b:
# If mid element of a is greater than mid element of b, we can safely ignore second half of a.
# Otherwise, we can ignore second half of b.
def kthlargest(a, b, k):
    if len(a) == 0:
        return b[k]
    elif len(b) == 0:
        return a[k]

    mid1 = len(a) // 2  # integer division
    mid2 = len(b) // 2
    if mid1 + mid2 < k:
        if a[mid1] > b[mid2]:
            return kthlargest(a, b[mid2 + 1:], k - mid2 - 1)
        else:
            return kthlargest(a[mid1 + 1:], b, k - mid1 - 1)
    else:
        if a[mid1] > b[mid2]:
            return kthlargest(a[:mid1], b, k)
        else:
            return kthlargest(a, b[:mid2], k)


# class MyTestCase(unittest.TestCase):
#     def test_2(self):
#         x = [5]
#         y = [2,4,6,8,10]
#         k = 1
#         actual = kthlargest(x,y, k)
#         expected = 4
#         self.assertEqual(expected, actual)
#     def test_3(self):
#         x = [1,3,5,7,9,11]
#         y = [2,4,6,8,10]
#         k = 4
#         actual = kthlargest(x,y, k)
#         expected = 5
#         self.assertEqual(expected, actual)
