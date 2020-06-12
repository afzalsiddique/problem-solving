#include<stdio.h>

int main()
{
    int n, i, j, store, no_taxi=0, seatleft=4;
    int num[100001];
    scanf("%d", &n);

    for (i = 0; i < n; i++)
    {
        scanf("%d", &num[i]);
    }

    for (i = 0; i < n; i++)
    {
        for (j = i+1; j < n; ++j)
        {
            if (num[i] > num[j])
            {
                store = num[i];
                num[i] = num[j];
                num[j] = store;
            }
        }
    }

    for (i = 0; i < n; )
    {
        if (num[i] <= seatleft)
        {
            seatleft-=num[i];
            i++;
        }
        else if (num[i] > seatleft)
        {
            no_taxi++;
            seatleft = 4;
        }
    }

    printf("%d", no_taxi+1);




//    printf("%d\t%d\t%d\t%d", count1, count2, count3, count4);


    return 0;
}
