#include<stdio.h>

int main()
{
    int n,i,sum=0,count=0,arr[100001];
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
        if(arr[i]>0)
            sum+=arr[i];

        if(!sum)
        {
            count++;
        }
        else if(arr[i]==-1)
        {
            sum--;
        }
    }
    printf("%d",count);




    return 0;
}
