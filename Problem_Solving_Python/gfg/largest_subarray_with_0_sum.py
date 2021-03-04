def maxLen(n, arr):
    di = {}
    curr_sum,maxx= 0,0
    for i in range(n):
        curr_sum += arr[i]
        if curr_sum==0: # [0,0,0,0], [-1,1,-1,1]
            maxx = i+1
        if curr_sum in di:
            maxx = max(maxx, i-di[curr_sum])
        else:
            di[curr_sum] = i
    return maxx
