#include<stdio.h>

int main()
{
    int n,m, smallest;
    scanf("%d%d", &n, &m);
    if(n<m)
        smallest=n;
    else
        smallest=m;

    if(smallest%2)
        printf("Akshat");
    else
        printf("Malvika");

    return 0;
}
