from collections import defaultdict


def subarrayXor(arr, n, k):
    ans,mp=0,defaultdict(int)
    xor = [0 for _ in range(n)]
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



def subarraySum(nums,n ,k):
    ans,mp=0,defaultdict(int)
    pre = [0 for _ in range(n)]
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