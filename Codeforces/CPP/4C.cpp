#include<bits/stdc++.h>
using namespace std;
int main()
{
    map<string, int>mp;
    int n;
    string s;
    cin >> n;
    while(n--)
    {
        cin >> s;
        if (mp.find(s)==mp.end())
        {
            mp[s]=0;
            cout<<"OK"<<endl;
        }
        else
        {
            mp[s]++;
            cout << s << mp[s]<<endl;
        }
    }
}
