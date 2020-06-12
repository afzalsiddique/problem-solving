#include<stdio.h>

int main()
{
    int a, b, c, r1, r2, r3, r4;
    scanf("%d %d %d", &a, &b, &c);

    r1 = a + b + c;
    r2 = (a+b) * c;
    r3 = a * (b+c);
    r4 = a * b * c;

    if (r1 >= r2 && r1 >= r3 && r1 >= r4)
    {
        printf("%d", r1);
    }
    else if (r2 >= r1 && r2 >= r3 && r2 >= r4)
    {
        printf("%d", r2);
    }
    else if (r3 >= r1 && r3 >= r2 && r3 >= r4)
    {
        printf("%d", r3);
    }
    else if (r4 >= r1 && r4 >= r2 && r4 >= r3)
    {
        printf("%d", r4);
    }




    return 0;
}
