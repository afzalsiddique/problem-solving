#include<stdio.h>

int main()
{
    int n,i,j,k;
    scanf("%d",&n);
    int arr[n+2][n+2];
    for(i=1; i<n+1; i++)
        for(j=1; j<n+1; j++)
            arr[i][j]=j*i;
    for(i=1; i<n+1; i++)
        {
            for(j=1; j<n+1; j++)
                printf("%d\t
                       ",arr[i][j]);
            printf("\n");
        }
    return 0;
}
