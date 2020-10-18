def f(t,n,d,i,j):
    if i==n-1:
        return t[i][j]
    if d[i][j]!=-1:
        return d[i][j]
    b=t[i][j]+f(t,n,d,i+1,j)
    r=t[i][j]+f(t,n,d,i+1,j+1)
    d[i][j]=max(b,r)
    return d[i][j]
for c in range(int(input())):
    t=[]
    n=int(input())
    d=[[-1]*n for _ in range(n)]
    for i in range(n):
        t.append(list(map(int, input().split())))
    print(f(t,n,d,0,0))
