#include <bits/stdc++.h>
using namespace std;

void createLPS(string pat, int lps[]){
    int j = 0, m = pat.length();
    lps[0] = 0;
    int i = 1;
    while(i < m){
        if(pat[i] == pat[j]){
            j++;
            lps[i] = j;
            i++;
        }
        else{
            if(j != 0)
                j = lps[j - 1];
            else{
                lps[i] = 0;
                i++;
            }
        }
    }
}

int KMPsearch(string text, string pattern){
    int lps[pattern.length()];
    createLPS(pattern, lps);
    int i, j, cnt = 0;
    for(i=0, j=0; i<text.length(); ){
        if(text[i] == pattern[j]){
            i++;
            j++;
        }
        if(j == pattern.length()){
            cnt++;
            j = lps[j-1];
        }
        else if(text[i] != pattern[j] && i < text.length()){
            if(j != 0)
                j = lps[j-1];
            else
                i++;
        }
    }
    return cnt;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t, q;
    cin >> t;
    for(q=0; q<t; q++){
        string a, b;
        cin >> a >> b;
        cout << "Case " << q+1 << ": " << KMPsearch(a,b) << '\n';
    }

    return 0;
}
