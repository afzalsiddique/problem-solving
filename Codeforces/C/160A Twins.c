#include<stdio.h>

int main()
{
    int n, money = 0, i, j, store, sumbytwo = 0;
    scanf("%d", &n);
    int coin[n+1];

    for (i = 0; i < n; i++)
    {
        scanf("%d", &coin[i]);
        sumbytwo += coin[i];
    }

    sumbytwo = sumbytwo/2;

    for (i = 0; i < n; i++)
    {
        for (j = i+1; j < n; j++)
        {
            if (coin[i] < coin[j])
            {
                store = coin[i];
                coin[i] = coin[j];
                coin[j] = store;
            }

        }
    }

//    for (i = 0; i < n; i++)
//    {
//        printf("%d\t", coin[i]);
//    }

    for (i = 0; money <= sumbytwo; i++)
    {
        money += coin[i];
    }

    printf("%d", i);


    return 0;
}
