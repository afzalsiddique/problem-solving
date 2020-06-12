#include <bits/stdc++.h>
using namespace std;

int main()
{
    set<int> costs;
    map<string, int> itemData;
    map<int, string> items;
    int n, type, cost;
    string name;
    cin >> n;
    for(int i=1; i<=n; i++)
    {
        cin >> type;
        if (type==1)
        {
            cin >> name>> cost;
            costs.insert(cost);
            items[cost]=name;
            itemData[name]=cost;
        }
        else if (type==2)
        {
            cin >> name>> cost;
            int temp;
            temp=itemData[name];
            costs.erase(temp);
            itemData[name]=cost;
            items[cost]=name;
            costs.insert(cost);
        }
        else
        {
            string buy;
            cin >> buy;
            cost = *(costs.begin());
            cout << items[cost] << " " << i << endl;
            name=items[cost];
            costs.erase(cost);
            items.erase(cost);
            itemData.erase(name);
        }
    }
    return 0;
}
