#include<stdio.h>

int mod(int a, int i)
{
    if(a>i)
        return (a-i);
    else
        return (i-a);
}

int main()
{
    int a,b,c,sum,i,farthest,minimum=301;
    scanf("%d%d%d",&a,&b,&c);
    if(a>b && a>c)
        farthest=a;
    else if(b>a && b>c)
        farthest=b;
    else if(c>a && c>b)
        farthest=c;

    for(i=1;i<=farthest;i++)
    {
        sum=mod(a,i)+mod(b,i)+mod(c,i);
//        printf("%d\n",sum);
        if(sum<minimum)
            minimum=sum;
    }
    printf("%d",minimum);

    return 0;
}
