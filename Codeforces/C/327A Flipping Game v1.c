#include<stdio.h>

int main()
{
    int n,i,count1=0,sum=0,max=0,a;

    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf("%d",&a);
        if(sum<0)
            sum=0;
        if(a==0)
            sum++;
        else
            {
                count1++;
                sum--;
            }
        if(max<sum)
            max=sum;

    }
    printf("%d", max+count1);



    return 0;
}
