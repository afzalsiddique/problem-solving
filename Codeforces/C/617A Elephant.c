#include<stdio.h>

int main()
{
    long x;
    scanf("%ld", &x);
    if(x%5!=0)
        printf("%ld", x/5+1);
    else
        printf("%ld", x/5);




    return 0;
}
