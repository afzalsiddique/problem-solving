#include<bits/stdc++.h>
using namespace std;
short dp[5001][5001];
int main()
{
    int n, i, j;
    string a,b;
    cin >> n;
    cin >> a;
    b = a;
    reverse(b.begin(),b.end());
    memset(dp,0,sizeof dp);
    for(i=1;i<=n;i++){
        for(j=1;j<=n;j++){
            if (a[i-1]==b[j-1])
                dp[i][j] = dp[i-1][j-1]+1;
            else
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
        }
    }
    cout << n - dp[n][n];
    return 0;
}
