from collections import defaultdict


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



    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        di = {x:False for x in "abcdefghijklmnopqrstuvwxyz"}
        l,r=0,0
        while True:
            if di[s[r]]==True:
                break
            di[s[r]]=True
            r+=1
        maxx = r-l
        while r<n:
            if di[s[r]]==True:
                di[s[l]]=False
                l+=1
            else:
                di[s[r]] = True
                r+=1
            maxx=max(maxx,r-l)
        return maxx