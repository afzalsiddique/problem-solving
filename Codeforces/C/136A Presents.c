#include<stdio.h>

int main()
{
    int n,i,j,count=0;
    scanf("%d", &n);
    int p[n+2];
    int ans[n+2];
    for(i=1; i<n+1; i++)
        scanf("%d",&p[i]);

    for(i=1,j=1; count!=n; )
    {
        if(p[i]!=j)
        {
            i++;
        }
        else
        {
            ans[j] = i;
            j++;
            i=1;
            count++;
        }
    }

    for(i=1; i<n+1; i++)
        printf("%d ",ans[i]);


    return 0;
}
