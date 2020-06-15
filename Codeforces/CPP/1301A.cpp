#include <bits/stdc++.h>
#define FOR(i,n) for(int i=0;i<n;i++)
using namespace std;

int main()
{
    string a,b,c;
    int n;
    cin >> n;
    while(n--)
    {
        cin >> a >> b >> c;
        bool flag=1;
        for (int i=0; i< a.size(); i++)
        {
            swap(c[i],a[i]);
            if (a[i]==b[i])
                continue;
            else
                swap(c[i],a[i]);
            swap(c[i],b[i]);
            if (a[i]==b[i])
                continue;
            else
            {
                flag=0;
                break;
            }
        }
        if (flag)
            cout << "Yes" << endl;
        else
            cout <<"No" << endl;
    }

    return 0;
}
