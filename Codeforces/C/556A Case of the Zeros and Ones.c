#include<stdio.h>

int main()
{
    int n,i,count1=0,count0=0;
    scanf("%d",&n);
    char str[n+1];
    for(i=0; i<n; i++)
    {
        fflush(stdin);
        scanf("%c",&str[i]);
        if(str[i]=='0')
        {
            count0++;
            printf("i: %d\tcount0: %d\n",i,count0);
        }
        else if(str[i]=='1')
        {
            count1++;
            printf("i: %d\tcount1: %d\n",i,count1);
        }
    }
    if(count0>count1)
        printf("%d",count0-count1);
    else if(count1>count0)
        printf("%d",count1-count0);
    else
        printf("%d",0);



    return 0;
}
