#include<stdio.h>
int main()
{
    int n,i,j,k,count=0;
    long x;
    scanf("%d%ld",&n,&x);
    for(i=1; i<n+1; i++)
        for(j=1; j<n+1; j++)
            if(i*j==x)
                count++;
    printf("%d",count);
    return 0;
}
