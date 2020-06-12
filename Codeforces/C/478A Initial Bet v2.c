#include<stdio.h>

int main()
{
    int coin[6],*p=coin,i=5,sum=0;
    float res1,res2;
    while(i--)
    {
        scanf("%d",p);
        sum+=*p;
        p++;
    }
    printf("%d\n",sum);
    res1=(int)(sum/5);
    res2=sum/5.0;
    if(res1==res2)
        printf("%d",res2);
    else
        printf("%d",-1);




    return 0;
}
