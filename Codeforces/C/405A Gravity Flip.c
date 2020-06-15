#include<stdio.h>

int main()
{
    int n, i, j, store;
    scanf("%d", &n);
    int a[n+1];

    for(i=0; i<n; i++)
    {
        scanf("%d", &a[i]);
    }

    for(i=0; i<n; i++)
    {
        for(j=i+1; j<n; j++)
        {
            if(a[i]>a[j])
            {
                store=a[i];
                a[i]=a[j];
                a[j]=store;
            }
        }
    }

    for(i=0; i<n; i++)
    {
        printf("%d ", a[i]);
    }

    return 0;
}
