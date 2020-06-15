#include<stdio.h>

int main()
{
    int currentcandle, added, remaining, sum = 0, b; //sum = added + remaining
    scanf("%d%d", &currentcandle, &b);
    sum = currentcandle;

    for( ; ; )
    {
        added = currentcandle / b;
        remaining = currentcandle % b;
        sum = sum + added;
        currentcandle = added + remaining;

        if(currentcandle == b-1)
        {
            printf("%d", sum);
            break;
        }
        else if (currentcandle == 1)
        {
            printf("%d", sum);
            break;
        }

    }



    return 0;
}
