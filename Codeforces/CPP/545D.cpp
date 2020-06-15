#include<bits/stdc++.h>
#define FOR(i,n)     for(int i=0;i<n;i++)
using namespace std;
int main()
{
    int n,total=0, cnt=0;//first is never disappointed
    cin >> n;
    int arr[n];
    FOR(i,n) cin >> arr[i];
    sort(arr,arr+n);
    FOR(i,n)
    {
        if (total <= arr[i]){
            cnt++;
            total+=arr[i];
        }
    }
    cout << cnt<< endl;
    return 0;
}
