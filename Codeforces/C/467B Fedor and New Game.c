#include<stdio.h>

int main()
{
    int n,m,k,i,count=0;
    scanf("%d %d %d",&n,&m,&k);
    int army[m+2];
    for(i=0; i<=m; i++)
        scanf("%d",&army[i]);
    for(i=0; i<m; i++)
    {
        {
            if(  (army[i]-army[m]) <= k  || (army[m]-army[i]) <= k  )
                count++;
        }
        printf("%d\n",count);
    }



    return 0;
}
