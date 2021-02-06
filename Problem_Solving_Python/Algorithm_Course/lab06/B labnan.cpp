#include<bits/stdc++.h>
#define MAX_NODES 110

using namespace std;
int numberOfNodes,pr[MAX_NODES],cap[MAX_NODES][MAX_NODES];


int bfs(int src,int des)
{
    int vis[MAX_NODES]= {0};
    vis[src]=1;
    pr[src]=-1;
    queue<int>Q;
    Q.push(src);

    while(!Q.empty())
    {
        int u=Q.front();
        Q.pop();
        for(int i=1; i<=numberOfNodes; i++)
        {
            if(vis[i] or cap[u][i]<=0) continue;
            Q.push(i);
            vis[i]=1;
            pr[i]=u;

        }
    }

    return vis[des];
}
int maxFlow(int src,int des)
{
    int f=0;
    while(bfs(src,des))
    {

        int path=1e9;
        for(int i=des; i!=src; i=pr[i]) path=min(path,cap[pr[i]][i]);

        for(int i=des; i!=src; i=pr[i])
        {

            int u=pr[i];
            int v=i;

            cap[u][v] -= path;
            cap[v][u] += path;

        }

        f+=path;

    }
    return f;
}



int main()
{
    int edges,src,des,cs = 0, t;
    cin>>t;

    while (t--)
    {
        memset(cap,0, sizeof(cap));
        memset(pr,0, sizeof(pr));
        cin>>numberOfNodes>>src>>des>>edges;
        for(int i=0;i<edges;i++)
        {
            int u,v,capacity;
            cin >> u >> v >> capacity;
            cap[u][v]+=capacity;
            cap[v][u]+=capacity;
        }
        cout <<"Case "<<++cs<<": "<< maxFlow(src,des) << "\n";
    }

}
