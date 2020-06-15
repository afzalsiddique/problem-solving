#include<stdio.h>

int main()
{
    int n,i,j,count=0,smallest,largest;
    scanf("%d",&n);
    int point[n+1];
    for(i=0;i<n;i++)
        scanf("%d",&point[i]);
    smallest=point[0];
    largest=point[0];


    for(i=1;i<n;i++)
    {
        if(point[i]<smallest)
        {
            smallest=point[i];
            count++;
        }
            if(point[i]>largest)
        {
            largest=point[i];
            count++;
        }

    }
    printf("%d",count);


    return 0;
}
