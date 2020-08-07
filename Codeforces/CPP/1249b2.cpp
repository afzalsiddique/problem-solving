//https://www.youtube.com/watch?v=7sNLifVSn4c

#include<bits/stdc++.h>
using namespace std;

int parent[200005], sizeDSU[200005];
void make_set(int v){
    parent[v] = v;
    sizeDSU[v] = 1;
}

int find_set(int v){
    if(v == parent[v])
        return v;
    return parent[v] = find_set(parent[v]);
}

void union_sets(int a, int b) {
    a = find_set(a);
    b = find_set(b);
    if (a != b) {
        if (sizeDSU[a] < sizeDSU[b])
            swap(a, b);
        parent[b] = a;
        sizeDSU[a] += sizeDSU[b];
    }
}

int main()
{
    int q, i,representative,n;
    cin >> q;
    while(q--){
        cin >> n;
        int partner[n+2];
        for(i = 1; i <= n; i++){
            cin >> partner[i];
            make_set( partner[i]);
        }
        for(i = 1; i <= n; i++)
            union_sets(i, partner[i]);

        for(i = 1; i <= n; i++){
            representative = find_set(partner[i]);
            cout << sizeDSU[representative] << " ";
        }
        cout << endl;
    }
}
