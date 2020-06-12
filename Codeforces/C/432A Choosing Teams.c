#include<stdio.h>

int main()
{
    int n,k,i,count=0,temp;
    scanf("%d%d",&n,&k);
    for(i=0;i<n;i++)
    {
        scanf("%d",&temp);
        if(5-temp>=k)
        {
            count++;
        }
    }
    printf("%d",count/3);



    return 0;
}
