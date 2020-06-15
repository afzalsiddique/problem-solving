#include<stdio.h>

int main()
{
    long long n,result1,result2;
    scanf("%lld",&n);

    if(n>=0)
    {
        printf("%d",n);
    }
    else
    {
        result1=n/100;
        result1*=10;
//        printf("%d\n",result1);
        result1=result1+n%10;
//        printf("%d\n",result1);
        result2=n/10;
//        printf("result1: %lld\tresult2: %lld\n",result1,result2);
        if(n==-10)
            printf("%d",0);
        else if(result1>result2)
            printf("%lld",result1);
        else
            printf("%lld",result2);;
    }



    return 0;
}
