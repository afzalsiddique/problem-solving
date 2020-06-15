#include<stdio.h>

int main()
{
    int n,t,i;
    scanf("%d%d",&n,&t);
    if(t==2 || t==4 || t==8 || t==3 || t==6 || t==9 || t==5 || t==7)
    {
        for(i=0; i<n; i++)
            printf("%d",t);
    }
    else if(t==10)
    {
        if(n==1)
            printf("%d",-1);
        else
        {
            for(i=0; i<n-1; i++)
                printf("%d",1);
            printf("%d",0);
        }
    }


    return 0;
}
