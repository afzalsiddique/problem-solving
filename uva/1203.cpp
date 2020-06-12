#include<bits/stdc++.h>
using namespace std;
typedef pair<int,int> pi;
int main()
{
    int k;
    priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>> > pq;
    while(1)
    {
        string input;
        cin >> input;
        if (input == "#")
            break;
        int reg, freq;
        cin >> reg >> freq;
        for (int i = 1; freq*i <= 10000; i++)
        {
            pq.push(make_pair(freq*i, reg));
        }
    }
    cin >> k;
    for(int i=0; i<k; i++)
    {
        pair<int,int>top = pq.top();
        pq.pop();
        cout << top.second << endl;
    }
    return 0;
}
