#include<stdio.h>

int main()
{
    long long number;
    scanf("%lld", &number);
    if(number%2!=0)
        printf("-%lld", (number+1)/2);
    else
        printf("%lld", number/2);



    return 0;
}
