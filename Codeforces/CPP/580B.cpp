#include <bits/stdc++.h>
#define FOR(i, n) for (int i = 0; i < n; i++)
using namespace std;
main()
{
    vector<pair<int, int>> v;
    int n, difference, money, ffactor;
    cin >> n >> difference;
    FOR(i, n)
    {
        cin >> money >> ffactor;
        v.push_back(make_pair(money, ffactor));
    }
    sort(v.begin(), v.end());
    long long maximum = -1, sum = 0;
    for (int i = 0, j = 0; i < n;)
    {
        if (v[i].first - v[j].first < difference)
        {
            sum += v[i].second;
            i++;
        }
        else
        {
            sum -= v[j].second;
            j++;
        }
        maximum = max(maximum, sum);
    }
    cout << maximum;
}