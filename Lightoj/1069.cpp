#include<stdio.h>
int main()
{
    int t, i, totalfloor = 0;
    scanf("%d", &t);
    int lift[t+2];
    int person[t+2];
    for (i = 0; i < t; i++)
    {
        scanf("%d %d", &person[i], &lift[i]);
    }
    for (i = 0; i < t; i++)
    {
        if (person[i]<lift[i])
        {
            totalfloor = lift[i];
        }
        else
        {
            totalfloor = person[i] - lift[i] + person[i];
        }
        printf("Case %d: %d\n", i+1, (totalfloor*4)+19);
    }
    return 0;
}
