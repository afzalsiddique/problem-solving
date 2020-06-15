#include<stdio.h>

int main()
{
    int coin[6],*p=coin,i=5,sum=0;
//    float res1,res2;
    while(i--)
    {
        scanf("%d",p);
        sum+=*p;
        p++;
    }
//    printf("%d\n",sum);
    if(sum%5==0 && sum!=0)
        printf("%d",sum/5);
    else
        printf("%d",-1);




    return 0;
}
