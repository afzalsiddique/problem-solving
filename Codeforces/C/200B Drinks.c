#include<stdio.h>

int main()
{
    int n,i=0;
    scanf("%d",&n);
    float temp,sum=0;
    for(i=0;i<n;i++)
    {
        scanf("%f",&temp);
        sum+=temp;
    }
    sum=(float)sum;
    printf("%f",sum/n);



    return 0;
}
