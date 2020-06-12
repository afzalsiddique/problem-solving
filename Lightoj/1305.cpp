#include<stdio.h>

int main()
{
    int t, i;
    scanf("%d", &t);
    int ax[1002];
    int ay[1002];
    int bx[1002];
    int by[1002];
    int cx[1002];
    int cy[1002];
    int dx[1002];
    int dy[1002];
    int area[1002];

    for (i = 0; i < t; i++)
    {
        scanf("%d %d %d %d %d %d", &ax[i], &ay[i], &bx[i], &by[i], &cx[i], &cy[i]);
        dx[i] = cx[i] - ( bx[i] - ax[i] );
        dy[i] = ay[i] + ( cy[i] - by[i] );
        area[i] = (ax[i]*by[i]+bx[i]*cy[i]+cx[i]*dy[i]+dx[i]*ay[i] -
                  ay[i]*bx[i]-by[i]*cx[i]-cy[i]*dx[i]-dy[i]*ax[i]) /2;
    }

    for (i = 0; i < t; i++)
    {
        if (area[i] < 0)
        {
            printf("Case %d: %d %d %d\n", i+1, dx[i], dy[i], -(area[i]));
        }
        else
        {
            printf("Case %d: %d %d %d\n", i+1, dx[i], dy[i], area[i]);
        }
    }



    return 0;
}
