from collections import deque, defaultdict



class Solution:
    def subarraySum(self, nums ,k):
        ## best example for thinking process ##
        # [3,4,7,2,-3,1,4,2,-13,0,7], k= 7
        n = len(nums)
        ans,mp=0,defaultdict(int)
        pre = [0 for _ in range(n)]# could be replaced by currentSum. no need for this array
        pre[0] = nums[0]
        for i in range(1,n):
            pre[i] = pre[i-1] + nums[i]
        for i in range(n):
            if pre[i] == k:
                ans+=1
            y = pre[i] - k
            if y in mp:
                ans+=mp[y]
            mp[pre[i]]+=1
        return ans
