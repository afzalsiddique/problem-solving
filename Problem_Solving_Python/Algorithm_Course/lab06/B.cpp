#include<bits/stdc++.h>

using namespace std;
const int maxnodes = 100;
int n, pr[110], cap[110][110];


int bfs(int src,int des)
{
    int vis[110]= {0};
    vis[src]=1;
    pr[src]=-1;
    queue<int>Q;
    Q.push(src);

    while(!Q.empty())
    {
        int u=Q.front();
        Q.pop();
        for(int i=1; i<=n+2; i++)
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



int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int totalTest;
    cin >> totalTest;
    for(int test=0; test<totalTest; test++){
        int noOfRegulators;
        cin >> noOfRegulators;
        int regCap[noOfRegulators+1];
        for(int i=0;i<noOfRegulators;i++){
            cin >> regCap[i];
        }
        int m;
        cin >> m;
        for(int i=0;i<m;i++){
            int u,v,tmp;
            cin >> u >> v >>tmp;
            cap[u][v]=tmp;
        }
        int barisal, dhaka;
        cin >> barisal >> dhaka;
        for(int i=0;i<barisal;i++){
            int tmp;
            cin >> tmp;

        }
        int m,s,t;
        cin >> n >> s >> t >> m;

        for(int i=0; i<n+1; i++){
            for(int j=0; j<n+1; j++){
                cap[i][j] = 0;
            }
        }

        for(int i=0;i<m;i++){
            int a,b,c;
            cin >> a >> b >> c;
            cap[a][b]+=c;
            cap[b][a]+=c;
        }
        cout <<"Case "<< test+1 <<": "<< maxFlow(s,t) << "\n";
    }

    return 0;
}

