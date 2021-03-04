# same as activity selection

s = [1,3,1,3,0,5,8,5]
f = [2,4,2,4,6,7,9,9]
def maximumMeetings(n, s, f):
    meetings = [(s[i],f[i]) for i in range(n)]
    meetings.sort(key=lambda x:x[1]) # sort meetings according to finsh time
    last=-1
    cnt=0
    for start,end in meetings:
        if start>last:
            cnt+=1
            last=end
    return cnt

print(maximumMeetings(len(s),s,f))