#include<stdio.h>
int main()
{
    int n, lucky[10]={4,7,44,47,74,77,444,447,474,477},i,flag=0;
    scanf("%d",&n);
    for(i=0;i<10;i++)
        if(n%lucky[i]==0)flag=1;
    if(flag)printf("YES");
    else printf("NO");
    return 0;
}
