#include<stdio.h>

int main()
{
    int n,i,count=1;
    scanf("%d",&n);
    int m[n+1];
    for(i=0;i<n;i++)
        scanf("%d",&m[i]);
    for(i=0;i<n-1;i++)
        {
            if(m[i]!=m[i+1])
                count++;
        }
    printf("%d",count);



    return 0;
}
