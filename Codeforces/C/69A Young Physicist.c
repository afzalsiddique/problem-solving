#include<stdio.h>

int main()
{
    int n, i, sumx=0, sumy=0, sumz=0;
    int x[101];
    int y[101];
    int z[101];

    scanf("%d", &n);

    for (i = 0; i < n; i++)
    {
        scanf("%d %d %d", &x[i], &y[i], &z[i]);
        sumx += x[i];
        sumy += y[i];
        sumz += z[i];
    }

    if (sumx == 0 && sumy== 0 && sumz== 0)
        printf("YES");
    else
        printf("NO");



    return 0;
}
