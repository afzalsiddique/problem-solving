#include<bits/stdc++.h>
using namespace std;
int main()
{
    map<pair<int,int>,string> mp;
    int n, t, code1, code2;
    string name;
    cin >> n;
    for(int i=0;i<n;i++)
    {
        cin >> code1 >> code2;
        cin >> name;
        pair<int,int> code = make_pair(code1,code2);
        mp[code]=name;
    }
    cin >> t;
    for(int i=0;i<t;i++)
    {
        cin >> code1 >> code2;
        pair<int,int> w = make_pair(code1,code2);
        cout << mp[w]<< endl;
    }

}
