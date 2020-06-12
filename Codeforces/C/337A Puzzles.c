#include<stdio.h>

int main()
{
    int n, m, i, j, smallest=1001, diff, store, temp;
    scanf("%d %d", &n, &m);
    int pieces[m+1];

    for (i = 0; i < m; i++)
    {
        scanf("%d", &pieces[i]);
    }

    for (i = 0; i < m; i++)
    {
        for (j = i+1; j < m; j++)
        {
            if (pieces[i]>pieces[j])
            {
                store=pieces[i];
                pieces[i]=pieces[j];
                pieces[j]=store;
            }
        }
    }

    for(i=0; i<(m-n+1); i++)
    {
        temp= pieces[i+(n-1)] - pieces[i];
//        printf("temp: %d\n", temp);
        if (temp<smallest)
            {
                smallest=temp;
//                printf("smallest: %d\t temp: %d\n", smallest, temp);
            }
    }

    printf("%d", smallest);

    return 0;
}
