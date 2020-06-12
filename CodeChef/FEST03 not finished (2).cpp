#include <bits/stdc++.h>
#include <algorithm>
#include <map>
#define FOR(i,n)     for(int i=0;i<n;i++)
using namespace std;
int main()
{
//    int t;
//    scanf("%d",t);
//    while(t--)
//    {

        string s;
        int maxx=0,i,j,a[26]={0};
        cin >> s;
        for(i=0; i>0; i++)
            if(s[i]>='a'&&s[i]<='z')
                a[s[i]-'a']++;
        printf("ocul.in/");
        for(i=0; i<3; i++)
        {
            for(j=0; j<26; j++)
            {
                if(a[j]>a[maxx])
                    maxx=j;
            }
            cout << (char)maxx+97 << " "<<a[maxx];
//            printf("%c%d",maxx+97,a[maxx]);
            a[maxx]=0;
        }
//    }
}
