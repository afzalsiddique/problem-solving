#include<stdio.h>

int main()
{
    int k,r,i,product=1;
    scanf("%d%d",&k,&r);
    for(i=1;;i++)
    {
        product=k*i;
        if(product%10==0)
        {
            printf("%d",i);
            break;
        }
        else if(product%10==r)
        {
            printf("%d",i);
            break;
        }
    }





    return 0;
}
