#include<iostream>
#define FOR(i,n) for(int i=0;i<n;i++)
using namespace std;
int main()
{
    int t;
    cin >> t;
    while(t--)
    {
        int x, y, a, b, diff, sum;
        cin >> x >> y >> a >> b;
        diff = y - x;
        sum = a + b;
        if (diff%sum==0)
            cout << diff/sum << endl;
        else
            cout << "-1" << endl;
    }
}
