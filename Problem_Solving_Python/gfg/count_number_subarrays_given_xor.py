from collections import defaultdict

def subarrayXor(arr, n, k):
    ans = 0
    mp = defaultdict(int)
    xor = [0 for _ in range(n)]
    curr_xor = arr[0]
    for i in range(1,n):
        xor[i] = xor[i-1] 
    for i in range(n):
        curr_xor ^= arr[i]
        if curr_xor == k:
            ans+=1
        y = k ^ curr_xor
        if y in mp:
            ans += mp[y]
        mp[curr_xor] += 1

    return ans



def subarrayXor(arr, n, k):
    ans = 0
    mp = defaultdict(int)
    curr_xor = 0
    for i in range(n):
        curr_xor ^= arr[i]
        if curr_xor == k:
            ans+=1
        y = k ^ curr_xor
        if y in mp:
            ans += mp[y]
        mp[curr_xor] += 1

    return ans
arr = [4, 2, 2, 6, 4]
n = len(arr)
k = 6
print("Number of subarrays having given XOR is",
      subarrayXor(arr, n, k))

# for comparison
# largest subarray with 0 sum
def maxLen(n, arr):
    di = {}
    curr_sum,maxx= 0,0
    for i in range(n):
        curr_sum += arr[i]
        if curr_sum==0: # [-1,1,-1,1]
            maxx = i+1
        if curr_sum in di:
            maxx = max(maxx, i-di[curr_sum])
        else:
            di[curr_sum] = i
    return maxx



