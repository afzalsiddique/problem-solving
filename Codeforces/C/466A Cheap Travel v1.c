#include<stdio.h>

int main()
{
    int n,m,single,pack,result;
    scanf("%d%d%d%d",&n,&m,&single,&pack);
    if(pack/m>=single)
        printf("%d",single*n);
    else if(pack<=single)
    {
        if(n%m==0)
            printf("%d",n/m*pack);
        else
            printf("%d", (n/m+1)*pack );
    }
    else
    {
        if(n%m==0)
        {
            printf("%d",n/m*pack);
        }
        else
        {
            if(m>n)
                printf("%d",pack);
            else
            {
                result=n/m*pack + (n%m) * single;
                printf("%d",result);
            }

        }
    }




    return 0;
}
