#include<stdio.h>

int main()
{
    int currentcandle, added, remaining, sum = 0, b; //sum = added + remaining
    scanf("%d%d", &currentcandle, &b);
    sum = currentcandle;

    for( ; currentcandle > b-1 ; )
    {
        added = currentcandle / b;
        remaining = currentcandle % b;
        sum += added;
        currentcandle = added + remaining;
    }
    printf("%d", sum);

    return 0;
}
