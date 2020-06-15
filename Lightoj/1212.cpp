#include<bits/stdc++.h>
#include<deque>
#define FOR(i,n)     for(int i=0;i<n;i++)
using namespace std;
int main()
{
    int t;
    cin >> t;
    for(int caseNO=1; caseNO<=t; caseNO++)
    {
        cout << "Case " << caseNO << ":" << endl;
        int n,m,x,currentSize=0;
        deque<int> dq;
        string cmd;
        cin >> n >> m;
        while(m--)
        {
            cin >> cmd;
            if (cmd=="pushLeft")
            {
                cin >> x;
                if (currentSize==n)
                    cout << "The queue is full" << endl;
                else
                {
                    dq.push_front(x);
                    cout << "Pushed in left: " << x << endl;
                    currentSize++;
                }
            }
            else if (cmd=="pushRight")
            {
                cin >> x;
                if (currentSize==n)
                    cout << "The queue is full" << endl;
                else
                {
                    dq.push_back(x);
                    cout << "Pushed in right: " << x << endl;
                    currentSize++;
                }
            }
            else if (cmd=="popLeft")
            {
                if (currentSize==0)
                    cout << "The queue is empty" << endl;
                else
                {
                    cout << "Popped from left: " << dq.front() << endl;
                    dq.pop_front();
                    currentSize--;
                }
            }
            else if (cmd=="popRight")
            {
                if (currentSize==0)
                    cout << "The queue is empty" << endl;
                else
                {
                    cout << "Popped from right: " << dq.back() << endl;
                    dq.pop_back();
                    currentSize--;
                }

            }
        }

    }
}
