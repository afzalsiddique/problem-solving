#include<stdio.h>

int main()
{
    int coin[6],*p=coin,i=5,sum=0;
    while(i)
    {
        scanf("%d",*p);
        sum+=*p;
        p++;
        i--;
    }




    return 0;
}
