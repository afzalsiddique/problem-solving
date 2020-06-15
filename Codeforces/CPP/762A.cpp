#include <bits/stdc++.h>
#define ll long long
#define FOR(i,n) for(int i=0;i<n;i++)
using namespace std;

void printvector(vector<unsigned long long int> const &a){
    for (unsigned long long int i=0; i<a.size();i++)
    {
        cout << a.at(i) << " ";
    }
}

int main()
{
    vector<unsigned long long int> v1, v2;
    unsigned long long int n, k, cnt=0;
    cin >> n >> k;
    for(unsigned long long int i=1; i*i<=n; i++)
    {
        if (n%i==0)
        {
            v1.push_back(i);
            if (i*i!=n)//comment this line and input: 4 2
                v2.push_back(n/i);
        }
    }

//    printvector(v1);
//    printvector(v2);
//    cout << endl;

    if (k>(v1.size()+v2.size()))
    {
            cout << "-1" <<endl;
            return 0;
    }

    /*input:
    4 2
    36 5
    */
    if (  (v1.size()+v2.size()) % 2 == 1  && k==v1.size() )
    {
        cout << v1[k-1];
        return 0;
    }

    if (  k<= (v1.size()+v2.size()) /2  )
    {
//        cout << endl << v1.size() <<"    test1" << endl;
        cout << v1[k-1];
    }
    else
    {
        reverse(v2.begin(), v2.end());
//        cout << endl << k-v1.size()-1 <<"    test2" <<endl;
        cout << v2[k-v1.size()-1];
    }

    return 0;
}
