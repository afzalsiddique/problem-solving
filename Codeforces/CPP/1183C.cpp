#include<iostream>
using namespace std;
int main()
{
    int q;
    cin >> q;
    int charge, turn, justplay, playandcharge, ans;
    while(q--)
    {
        cin >> charge >> turn >> justplay >> playandcharge;
        if (charge<= turn * playandcharge)
            cout << "-1" << endl;
        else if (charge / justplay > turn)
            {
                cout << turn << endl;
//                cout << "else if executed" << endl;
            }
        else
        {
//        total charge = ans * justplay + (turn - ans) * playandcharge + 1;
//        "+1" for strictly greater than
            ans = (charge - 1 - turn * playandcharge )/ (justplay - playandcharge);
            if (ans>turn)
                cout << turn;
            else
                cout << ans << endl;
        }
    }
}
