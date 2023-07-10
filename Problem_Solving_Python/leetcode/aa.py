t = int(input())
for _ in range(t):
    x,y=list(map(int,input().split()))
    cnt=x//(y*2)
    print(cnt)