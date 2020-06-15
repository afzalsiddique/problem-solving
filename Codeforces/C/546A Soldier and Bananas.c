#include<stdio.h>

int main()
{
    int k, w, i;
    long n, moneyneeded, sum = 0;
    scanf("%d %ld %d", &k, &n, &w);

    for (i = 1; i <= w; i++)
    {
        sum = sum + k * i;
    }
//    printf("%ld\n", sum);
//    printf("%d \t%ld \t %d\t %d\t", k, n, w, i);
    moneyneeded = sum - n;
    if (moneyneeded > 0)
    {
        printf("%ld", moneyneeded);
    }
    else
    {
        printf("%d", 0);
    }


    return 0;
}
