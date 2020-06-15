#include<bits/stdc++.h>
#include<map>
#define FOR(i,n)     for(int i=0;i<n;i++)
using namespace std;
int main()
{
    while(true)
    {

        int n;
        cin >> n;
        if (n)
        {
            string sub[6];
            map<string, int> mp;
            FOR(i,n)
            {
                cin >> sub[0] >> sub[1] >> sub[2] >> sub[3] >> sub[4];
                sort(sub,sub+5);
                string key;
                key = sub[0] + sub[1] + sub[2] + sub[3] + sub[4];
                mp[key]++;
            }
            int maxx=-1;
            for(auto itr:mp)
                if(itr.second>maxx)
                    maxx=itr.second;
            int counts=0;
            for(auto itr:mp)
                if(itr.second==maxx)
                    counts++;
            cout << maxx*counts << endl;
        }
        else
            break;
    }
}
