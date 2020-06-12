#include<stdio.h>

int main()
{
    int n, result = 0, i;
    char a[4];
    scanf("%d", &n);
    for (i = 0; i <n; i++)
    {
        scanf("%s", a);
        if (a[1] == '+')
        {
            result++;
        }
        else if (a[1] == '-')
        {
            result--;
        }
    }
    printf("%d", result);





    return 0;
}
