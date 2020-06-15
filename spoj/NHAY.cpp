#include <bits/stdc++.h>
#define ll long long
#define FOR(i,n) for(int i=0;i<n;i++)
using namespace std;
void computeLPSArray(char *pat, int patLen, int *lps)
{
    lps[0]=0;
    for(int i=1,j=0; i<patLen;)
    {
        if (pat[i]==pat[j])
        {
            j++;
            lps[i]=j;
            i++;
        }
        else
        {
            if (j!=0)
                j=lps[j-1];
            else
            {
                lps[i]=0;
                i++;
            }
        }
    }
}
void KMPSearch(char *pat, char *txt)
{
    int textLen = strlen(txt), patLen = strlen(pat);
    int lps[patLen],cnt=0;
    computeLPSArray(pat, patLen, lps);
    for(int i=0,j=0; i<textLen;)
    {
        if (txt[i]==pat[j])
        {
            i++;
            j++;
        }
        if (j==patLen)
        {
            cout << i-j << endl;
            j = lps[j-1];
            cnt++;
        }
        else if (i<textLen && txt[i]!=pat[j])
        {
            if (j!=0)
                j=lps[j-1];
            else
                i++;
        }
    }
    if (cnt==0)
        cout << "\n\n";
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int patLen;
    string txt2;
    while(cin>>patLen)
    {
        char pat[patLen+1];
        cin >> pat;
        cin >> txt2;
        int txt2Len=txt2.length();
        char txt[txt2Len+1];
        for(int i=0; i<txt2Len; i++)
            txt[i]=txt2[i];
        KMPSearch(pat, txt);
    }
    return 0;
}
