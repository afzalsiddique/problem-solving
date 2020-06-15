#include<stdio.h>

int main()
{
    int n, i, inside = 0, highest = 0;
    scanf("%d", &n);
    int down[n+1];
    int up[n+1];


    for (i = 0; i < n; i++)
    {
        scanf("%d", &down[i]);
        scanf("%d", &up[i]);
    }

    inside = up[0];

    for (i = 0; i < n-1; i++)
    {
        if (inside > highest)
        {
            highest = inside;
        }
        inside = inside - down[i+1] + up[i+1];
    }

    printf("%d", highest);

    return 0;
}
