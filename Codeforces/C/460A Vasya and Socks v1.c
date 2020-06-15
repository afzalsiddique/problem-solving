#include<stdio.h>

int main()
{
    int n, m;
    scanf("%d%d", &n,&m);
    if(n<m)
        printf("%d", n);
    else if(m==2)
        printf("%d", n*m-1);
    else if(m%2)
        printf("%d", n+(n/m)+1 );
    else
        printf("%d", n+(n/m) );




    return 0;
}
