#include<stdio.h>

int main()
{
    int n,m,count1,count2,i;
    scanf("%d%d",&n,&m);
    if(n%2==0)
    {
        count2=n/2;
        count1=0;
    }
    else
    {
        count2=n/2;
        count1=1;
    }
//    printf("count1: %d\tcount2: %d\n",count1,count2);
    while(1)
    {
        if(count1>n)
        {
            printf("%d",-1);
            break;
        }
        else
        {
            if( (count1+count2)%m == 0 )
            {
                printf("%d",count1+count2);
                break;
            }
            else
            {
                count2--;
                count1+=2;
            }
        }
    }



    return 0;
}
