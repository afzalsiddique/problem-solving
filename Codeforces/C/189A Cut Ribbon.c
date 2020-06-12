#include<stdio.h>

int main()
{
    int n,i,j,temp,count=0,flag1=1,flag2=1,flag3=1;
    scanf("%d",&n);
    int ribbon[4];
    for(i=0;i<3;i++)
        scanf("%d",&ribbon[i]);
    for(i=0;i<3;i++)
        for(j=i+1;j<3;j++)
            if(ribbon[i]>ribbon[j])
            {
                temp=ribbon[i];
                ribbon[i]=ribbon[j];
                ribbon[j]=temp;
            }
//    for(i=0;i<3;i++)
//        printf("%d\n",ribbon[i]);
    while(n>=ribbon[0])
    {
        if(flag1)
        {
            n-=ribbon[0];
            count++;
            flag1=0;
        }
        else if(flag2)
        {
            n-=ribbon[1];
            count++;
            flag2=0;
        }
        else if(flag3)
        {
            n-=ribbon[2];
            count++;
            flag3=0;
        }
    }
    printf("%d",count);
    return 0;
}
