def ford(src, dst, n, cap):
    pr=[0]*(n+3)

    def bfs():
        vis=[False]*(n+3)
        vis[src]=True
        pr[dst]=-1
        q=[src]
        while q:
            u=q.pop(0)
            vis[u]=True
            for i in range(1,n+3):
                if i==u or vis[i]==True or cap[u][i]<=0:
                    continue
                q.append(i)
                vis[i]=True
                pr[i]=u
        return vis[dst]

    f=0
    while bfs():
        path=float('inf')
        i=dst
        while i!=src: # for(int i=des; i!=src; i=pr[i]) path=min(path,cap[pr[i]][i]);
            path=min(path,cap[pr[i]][i])
            i=pr[i]


        i=dst
        while i!=src:
            cap[pr[i]][i]-=path
            cap[i][pr[i]]+=path
            i=pr[i]

        f+=path
    return f

# for case in range(int(input())):
#     n = int(input())
#     cap=[[0]*(n+1) for _ in range(n+1)]
#     src,dst,conn=list(map(int,input().split()))
#     for _ in range(conn):
#         u, v, c=list(map(int, input().split()))
#         cap[u][v]+=c
#         cap[v][u]+=c
#     ans = ford(src,dst,n,cap)
#     print("Case {}: {}".format(case+1,ans))