#include <bits/stdc++.h>
using namespace std;
int main()
{
    long n, time, temp;
    long long cnt=0, sum=0,maxm=-1;
    vector<int> v;
    cin >> n >> time;
    for (int i = 0; i < n; i++)
    {
        cin >> temp;
        v.push_back(temp);
    }
    for(int i=0,j=0;i<n;)
    {
        if (sum<time && v[i]+sum<=time)
        {
            sum+=v[i];
            cnt=i-j+1;
            //cout << "i  sum:"<<sum<<" i:"<<i<<" j:"<<j<< " cnt:"<<cnt << endl;
            i++;
        }
        else
        {
            sum-=v[j];
            j++;
            cnt=i-j+1;
            //cout << "j  sum:"<<sum<<" i:"<<i<<" j:"<<j<< " cnt:"<<cnt << endl;
        }
        maxm=max(maxm,cnt);
    }
    cout << maxm << endl;
}
