#include<stdio.h>

int main()
{
    int n,h,i,sum=0,temp;
    scanf("%d%d",&n,&h);
    for(i=0;i<n;i++)
    {
        scanf("%d",&temp);
        if(temp>h)
            sum+=2;
        else
            sum++;
    }
    printf("%d",sum);




    return 0;
}
