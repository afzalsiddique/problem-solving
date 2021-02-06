#include<bits/stdc++.h>

using namespace std;
int n,pr[210],cap[210][210];


int entryPositionOfNode(int nodeToEnter);

int exitPositionOf(int exitingNode);

int bfs(int src, int des)
{
    int vis[210]= {0};
    vis[src]=1;
    pr[src]=-1;
    queue<int>Q;
    Q.push(src);

    while(!Q.empty())
    {
        int u=Q.front();
        Q.pop();
        for(int i=0; i<=2*(n+4); i++)
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

    int flow=0;
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

        flow+=path;

    }
    return flow;
}

void clear(){
    memset(pr, 0, sizeof(pr));
    memset(cap, 0, sizeof(cap));
}


int main()
{

    int test,cases=0;
    cin >> test;
    while(test--){

        int numberOfEdges,input;
        cin >> n;//4
        int source = 0;
        int sink = 2 * (n + 4);
        for (int i = 0; i < n;i++){
            cin >> input; //10,20,30,40
            int fromNode = 2 * i + 1; //1,3,5,7
            int toNode = fromNode + 1;//2,4,6,8
            cap[fromNode][toNode] += input;
            cap[toNode][fromNode] += input;
        }
        cin >> numberOfEdges;//6

        for (int i = 0; i < numberOfEdges; i++)
        {
            int inputFromNode, inputToNode,inputCapacity;        //1 1 1 2 2 3
            cin >> inputFromNode >> inputToNode >> inputCapacity;//2 3 4 3 4 4
            int exitingNode = exitPositionOf(inputFromNode); //2 2 2 4 4 6
            int entryNode = entryPositionOfNode(inputToNode); //3 5 7 5 7 7
            cap[exitingNode][entryNode] += inputCapacity;
        }

        int b, d;
        cin >> b >> d;

        for (int i = 0; i < b;i++){
            int inputToNode;
            cin >> inputToNode;
            int u = entryPositionOfNode(inputToNode);
            cap[source][u] = INT_MAX;
        }
        for (int i = 0; i < d;i++){
            int inputFromNode;
            cin >> inputFromNode;
            int u = exitPositionOf(inputFromNode);
            cap[u][sink] = INT_MAX;
        }

        cout << "Case " << ++cases << ": " << maxFlow(source, sink) << "\n";

        clear();
    }

}

int exitPositionOf(int exitingNode) { return 2 * exitingNode; }

int entryPositionOfNode(int nodeToEnter) { return 2 * nodeToEnter - 1; }
