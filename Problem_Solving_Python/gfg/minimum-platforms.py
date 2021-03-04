# https://www.youtube.com/watch?v=dxVcMDI7vyI&t=333s


def findPlatform(n, arr, dep):
    # I could be in the stations watching over all the platforms.
    # I only need to consider when highest no of trains are sitting in the platforms.
    # that's why arrivals and departures could be sorted individually
    arr.sort()
    dep.sort()
    cnt,maxx=0,0
    i,j=0,0
    while i!=n:
        if arr[i]<=dep[j]:
            cnt+=1
            i+=1
        else:
            cnt-=1
            j+=1
        maxx=max(maxx,cnt)
    return maxx

arrivals= [900, 940, 950, 1100, 1500, 1800]
departures=[ 910, 1200, 1120, 1130, 1900, 2000 ]
print(findPlatform(len(arrivals),arrivals,departures))


arrivals= [900, 940]
departures=[ 910, 1200]
print(findPlatform(len(arrivals), arrivals,departures))

arrivals= [1100, 1500, 1800]
departures=[1130, 1900, 2000]
print(findPlatform(len(arrivals), arrivals,departures))