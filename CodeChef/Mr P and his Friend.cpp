#include <bits/stdc++.h>
#include <algorithm>
#include <map>
#define FOR(i,n)     for(int i=0;i<n;i++)
using namespace std;
int main()
{
    int t;
    cin >> t;
    while(t--)
    {
        map<int,int> mp;
        int n;
        cin >> n;
        FOR(i,n)
        {
            int temp;
            cin >> temp;
            mp[temp]++;
        }
        int maxx=0;
        for(auto itr:mp)
        {
            if (itr.second>maxx)
                maxx=itr.second;
        }
        cout << n-maxx << endl;
    }
    return 0;
}
