#include<bits/stdc++.h>
#define FOR(i,n)     for(int i=0;i<n;i++)
using namespace std;
int main()
{
    map<int, int>mp;
    int n,m,ans=0, catalog;
    while(true)
    {
        cin >> n >> m;
        if (n==0 && m==0)
            break;
        FOR(i,n)
        {
            cin >> catalog;
            mp[catalog]++;
        }
        FOR(i,m)
        {
            cin >> catalog;
            mp[catalog]++;
        }
        ans=0;
        for(map<int, int>:: iterator it=mp.begin();it!=mp.end();it++)
        {
            if (it->second==2)
                ans++;
        }
        mp.clear();
        cout << ans << endl;
    }
    return 0;
}
