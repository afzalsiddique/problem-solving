#include<stdio.h>

int main()
{
    long long n, k;
    scanf("%lld %lld", &n, &k);
    if(n%2==0)
    {
        if(k<=(n/2))
        {
            printf("%lld", k*2-1);
        }
        else
        {
            k=k-(n/2);
            printf("%lld", k*2);
        }
    }
    else
    {
        if( k<=( (n/2)+1 ) )
        {
            printf("%lld", k*2-1);
        }
        else
        {
            k=k-( (n/2)+1 );
            printf("%lld", k*2);
        }

    }




    return 0;
}
