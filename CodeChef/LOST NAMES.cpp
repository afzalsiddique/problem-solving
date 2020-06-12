#include<bits/stdc++.h>
#include<map>
#define FOR(i,n)     for(int i=0;i<n;i++)
using namespace std;
int main()
{
    map<char, int> mp1,mp2;
    string first, second, all;
    bool flag = true;
    cin >> first;
    cin >> second;
    cin >> all;
    FOR(i, first.length())
        mp1[first[i]]++;
    FOR(i, second.length())
        mp1[second[i]]++;
    FOR(i, all.length())
        mp2[all[i]]++;
    auto itr1 = mp1.begin();
//    auto itr2 = mp2.begin();
    for(; itr1 != mp1.end(); itr1++)
    {
//        cout << itr->first << " " << itr->second << endl;
//        cout << mp1[itr1->first] << " " << mp2[itr1->first] << endl;
        if (mp1[itr1->first]>mp2[itr1->first])
        {
            flag = false;
            break;
        }
    }
    if (flag) cout << "YES";
    else cout << "NO";


    return 0;
}
