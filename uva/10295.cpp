#include<bits/stdc++.h>
#define FOR(i,n)     for(int i=0;i<n;i++)
using namespace std;
int sum=0;
map<string, int> mp;
void removeDupWord(string str)
{
    string word = "";
    for (auto x : str)
    {
        if (x == ' ')
        {
            if (mp.find(word)!=mp.end())
                sum+=mp[word];
            word = "";
        }
        else
        {
            word = word + x;
        }
    }
    if (mp.find(word)!=mp.end())
        sum+=mp[word];
}
int main()
{
    int n, m;
    cin >> n >> m;
    string word;
    int dollar;
    while(n--)
    {
        cin >> word >> dollar;
        mp[word] = dollar;
    }
    string str;
    while(m--)
    {
        while(true)
        {
            cin >> str;
            removeDupWord(str);
            if (str==".")
                break;

        }
        cout << sum << endl;
        sum=0;
    }
}
