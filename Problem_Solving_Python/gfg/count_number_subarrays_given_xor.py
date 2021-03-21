from collections import defaultdict

def subarrayXor(arr, n, k):
    ans,mp=0,defaultdict(int)
    xor = [0 for _ in range(n)] # could be replaced by currentXor. no need for this array
    xor[0] = arr[0]
    for i in range(1,n):
        xor[i] = xor[i-1] ^ arr[i]
    for i in range(n):
        if xor[i] == k:
            ans+=1
        y = k ^ xor[i]
        if y in mp:
            ans += mp[y]
        mp[xor[i]] += 1
    return ans

arr = [4, 2, 2, 6, 4]
n = len(arr)
k = 6
print("Number of subarrays having given XOR is",
      subarrayXor(arr, n, k))

# for comparison
# subarray sum equals to k

def subarraySum(nums,n ,k):
    ## best example for thinking process ##
    # [3,4,7,2,-3,1,4,2,-13,0,7], k= 7
    ans,mp=0,defaultdict(int)
    pre = [0 for _ in range(n)] # could be replaced by currentSum. no need for this array
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




