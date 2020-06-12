#include<bits/stdc++.h>
#include<map>
#define FOR(i,n)     for(int i=0;i<n;i++)
using namespace std;
int main()
{
    map<string, string> mp;
    string eng, foreign;
    getline(cin, eng);
    while(eng!="")
    {
        stringstream ss(eng);
        ss >> eng >> foreign;
        mp[foreign] =eng;
        getline(cin, eng);
    }
    map<string, string>::iterator itr;
    while(cin >> eng)
    {
        itr=mp.find(eng);
        if (itr==mp.end())
            cout << "eh" << endl;
        else
            cout << itr->second << endl;
    }

}
