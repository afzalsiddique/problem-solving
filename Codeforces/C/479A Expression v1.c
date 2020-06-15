#include<stdio.h>

int main()
{
    int a, b, c, result = 0;
    scanf("%d %d %d", &a, &b, &c);

    if (a==1 && b==1 && c==1)
    {
        printf("%d", a+b+c);
    }

    else if (a==1 && b==1)
    {
        printf("%d", ((a+b)*c) );
    }

    else if (a==1 && c==1)
    {
        printf("%d", ((a+c)*b) );
    }

    else if (c==1 && b==1)
    {
        printf("%d", ((c+b)*a) );
    }

    else if (a==1)
    {
        if (b<c)
        {
            printf("%d", ((a+b)*c) );
        }
        else
        {
            printf("%d", ((a+c)*b) );
        }
    }

    else if (b==1)
    {
        if (a<c)
        {
            printf("%d", ((a+b)*c) );
        }
        else
        {
            printf("%d", ((b+c)*a) );
        }
    }

    else if (c==1)
    {
        if (b<a)
        {
            printf("%d", ((b+c)*a) );
        }
        else
        {
            printf("%d", ((a+c)*b) );
        }
    }

    else
    {
        printf("%d", a*b*c);
    }


    return 0;
}
