def maxLen(n, arr):
    di,curr,ans={},0,0
    for i in range(0,n):
        curr+=arr[i]
        if curr==0:
            ans=i+1
        if curr not in di:
            di[curr] = i
        else:
            ans=max(ans, i-di[curr])
    return ans

arr = [15,-2,2,-8,1,7,10,23]
print(maxLen(len(arr),arr))
arr = [0,0,0,0]
print(maxLen(len(arr),arr))
arr = [-1,1,-1,1]
print(maxLen(len(arr),arr))
