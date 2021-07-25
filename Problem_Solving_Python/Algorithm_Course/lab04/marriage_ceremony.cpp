//https://vjudge.net/problem/LightOJ-1011
#include<bits/stdc++.h>
using namespace std;


int n;
int cost[17][17];
int dp[1<<17 -1][17];


int turnOn(int jobs,int job)
{
    return jobs | (1<<job);
}

bool isOn(int jobs,int job)
{
    return (bool)(jobs & (1<<job));
}

int call(int jobs,int workerNo)
{
    if(jobs == (1<<n) - 1) return 0;
    if(dp[jobs][workerNo]!=-1) return dp[jobs][workerNo];

    int ret = 0;

    for(int jobNo=0; jobNo<n; jobNo++)
    {
        if(isOn(jobs,jobNo)) continue;

        ret = max(ret, cost[workerNo][jobNo] + call(turnOn(jobs,jobNo),workerNo+1));

    }

    return dp[jobs][workerNo] = ret;

}


int main()
{
    int t;
    cin >> t;
    for(int caseNo=1;caseNo<=t;caseNo++)
    {
        cin>>n;
        for(int i=0; i<n; i++)
        {
            for(int j=0; j<n; j++)
                cin>>cost[i][j];
        }

        memset(dp,-1,sizeof(dp));
        cout<<"Case "<<caseNo<<": "<<call(0,0)<<endl;
    }
}



//2
//2
//1 5
//2 1
//3
//1 2 3
//6 5 4
//8 1 2