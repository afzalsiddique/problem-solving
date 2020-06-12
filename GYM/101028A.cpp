#include<stdio.h>

int main()
{
    int t,j;
    scanf("%d",&t);
    int n,r,i,sum,temp;
    for(j=0; j<t; j++)
    {
        scanf("%d%d",&n,&r);
        for(i=0,sum=1500; i<n; i++)
        {
            scanf("%d",&temp);
            sum+=temp;
        }
        if(sum==r)
            printf("Correct\n");
        else
            printf("Bug\n");

    }
    return 0;
}
