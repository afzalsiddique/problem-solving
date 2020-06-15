#include<stdio.h>

int main()
{
    int n, i, counter = 0;
    scanf("%d", &n);
    char peopleinroom[n+1];
    char roomcapacity[n+1];

    for (i = 0; i < n; i++)
    {
        scanf("%d %d", &peopleinroom[i], &roomcapacity[i]);
        if ( (roomcapacity[i] - peopleinroom[i]) >= 2 )
        {
            counter++;
        }
    }

    printf("%d", counter);

    return 0;
}
