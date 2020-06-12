#include<stdio.h>
int main()
{
    int n,i,j,k,count=0,x;
    scanf("%d%d",&n,&x);
    if(x==1)
        printf("%d",1);
    else
    {
        for(i=1;i<n+1;i++)
        {
            if(x%i==0 && i<=n && (x/i)<=n)
                count++;
        }
        printf("%d",count);
    }
    return 0;
}
