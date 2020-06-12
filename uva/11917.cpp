#include<bits/stdc++.h>
#include<map>
#include <iterator>
using namespace std;
int main()
{
    int t;
    cin >> t;
    for (int caseNo=1; caseNo<=t; caseNo++)
    {
        int n,days;
        string hw;
        cin >> n;
        map<string, int> mp;
        map<string, int>::iterator itr;
        while(n--)
        {
            string sub;
            int num;
            cin >> sub >> num;
            mp[sub]=num;
        }
//    for (itr = mp.begin(); itr != mp.end(); ++itr) {
//        cout << '\t' << itr->first
//             << '\t' << itr->second << '\n';
//    }
        cin >> days;
        cin >> hw;
//    cout << hw << " " << days <<endl;
        if (mp.find(hw)==mp.end())
            cout << "Case " << caseNo<< ": Do your own homework!" << endl;
        else if (mp[hw]<=days)
        {
//        cout << "mp[hw] "<< mp[hw] << "<=" <<"days " << days << endl;
            cout << "Case " << caseNo<< ": Yesss" << endl;
        }
        else if (mp[hw]<=days+5)
        {
//        cout << mp[hw] << "<=" << days+5;
            cout << "Case " << caseNo<< ": Late" << endl;
        }
        else{
            cout << "Case " << caseNo<< ": Do your own homework!" << endl;
        }
//    if(mp[hw]>=days+5)
//        cout << "Late" << endl;
//    else if(mp[hw]<=days)
//        cout << "Yesss" << endl;
//    else
//        cout << "Do your own" << endl;

//    map<string, int> time;
//    time["ai"]=3;
//    time["java"]=8;
//    auto it = time.find("a");
//    cout << it->first << "\t";
//    cout << it->second;
    }
    return 0;
}
