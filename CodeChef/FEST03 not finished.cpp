#include <bits/stdc++.h>
#include <algorithm>
#include <map>
#define FOR(i,n)     for(int i=0;i<n;i++)
using namespace std;
bool compare(const pair<int, int>&a, const pair<int, int>&b)
{
   return a.second<b.second;
}
int main(){
    map<char, int> mp;
    char a1,a2,a3;
    int n1,n2,n3;
    string str;
    cin >> str;
    FOR(i,str.length())
        mp[str[i]]++;
//    for(auto itr = mp.begin(); itr!=mp.end();itr++)
//    {
//        cout << itr->first << " " << itr->second << endl;
//        mp[itr->first]=-1;
//        cout << mp[itr->first] << endl;
    }
    mp['/'] = -1;
    mp['.'] = -1;
    auto max_itr = max_element(mp.begin(), mp.end(), compare);
    a1 = max_itr->first;
    n1 = max_itr->second;
    mp[max_itr->first] = -1;
    max_itr = max_element(mp.begin(), mp.end(), compare);
    a2 = max_itr->first;
    n2 = max_itr->second;
    mp[max_itr->first] = -1;
    max_itr = max_element(mp.begin(), mp.end(), compare);
    a3 = max_itr->first;
    n3 = max_itr->second;
    cout << "ocul.in/" <<a1<<n1<<a2<<n2<<a3<<n3;
    return 0;
}
