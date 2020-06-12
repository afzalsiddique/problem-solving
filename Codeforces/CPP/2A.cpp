#include<bits/stdc++.h>
#define FOR(i,n) for(int i=0;i<n;i++)
using namespace std;
int main()
{
    int n;
    cin >> n;
    map<string, int>finalScore;
    string name[n];
    int score[n], maximum=0;
    FOR(i,n)
    {
        cin >> name[i];
        cin >> score[i];
        finalScore[name[i]]+=score[i];
    }
    //all final scores of players are in finalScore map
    FOR(i,n)
    //maximum score after the game ends
        maximum=max(finalScore[name[i]], maximum);

    map<string, int> currentScore;
    FOR(i,n)
    {
        currentScore[name[i]]+=score[i];
        if (currentScore[name[i]]>=maximum && finalScore[name[i]]==maximum)
        {
            cout << name[i] << endl;
            break;
        }
    }
}
