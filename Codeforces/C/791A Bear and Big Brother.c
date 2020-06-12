#include<stdio.h>

int main()
{
    int a,b,i,count=0;
    scanf("%d %d",&a,&b);
    while(a<=b)
    {
        count++;
        a*=3;
        b*=2;
    }
    printf("%d",count);



    return 0;
}
