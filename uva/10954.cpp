#include<bits/stdc++.h>
#define FOR(i,n)     for(int i=0;i<n;i++)
using namespace std;
int main()
{
    int n, cost=0,sum=0;
    while(cin >> n)
    {
        if (n==0)
            break;
        priority_queue <int, vector<int>, greater<int> > pq;
        int temp;
        FOR(i,n)
        {
            cin >> temp;
            pq.push(temp);
        }
        cost=0;
        while(pq.size()>1)
        {
            sum=0;
            sum+=pq.top();
            pq.pop();
            sum+=pq.top();
            pq.pop();
            cost+=sum;
            pq.push(sum);
        }
        cout << cost << endl;

    }
    return 0;
}
