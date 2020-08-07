#include<bits/stdc++.h>
using namespace std;
 
long long parent[1000006];
long long size[1000006];
 
void make_set(int v)
{
    parent[v] = v;
    size[v] = 1;
}
 
int find_set(int v)
{
    if(v == parent[v])
        return v;
    return parent[v] = find_set(parent[v]);
}
 
void union_sets(int a, int b)
{
    int x = find_set(a);
    int y = find_set(b);
    if(x != y)
    {
      if(size[a] < size[b])
        swap(a, b);
 
      parent[b] = a;
      size[a] += size[b];
    }
}
 
int main()
{
    long long N,M,counter;
    int a, b;
    cin >> N >> M;
    counter = N;
    while(M--){
        cin >> a >> b;
        if(!parent[a])
            make_set(a);
        if(!parent[b])
            make_set(b);
        if(find_set(a)!=find_set(b)){
            counter--;
            union_sets(find_set(a),find_set(b));
        }
    }
    cout << counter << endl;
}
