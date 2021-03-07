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

sol = Solution()
x = [0,1,2,5,9]
y = [-2,-1,3,4,6,8]
k = 4
print(sol.kthElement(x, y,len(x),len(y), k), 5)
x = [1,10,10,25,40,54,79]
y = [15, 24, 27, 32, 33, 39, 48, 68, 82, 88, 90]
k = 15
print(sol.kthElement(x, y,len(x),len(y), k), 15)
