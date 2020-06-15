#include<stdio.h>

int main()
{
    int n, t, i, j, istore;
    scanf("%d %d", &n, &t);
    char string[n+1];
    scanf("%s", string);
    char store;

    for (i = 0; i < t; i++)
    {
        istore = i;
        for (j = i + 1; j < n-1; j++, i++)
        {
            if (string[i] < string[j])
            {
                store = string[i];
                string[i] = string[j];
                string[j] = store;
            }
        }
        i = istore;
    }

    printf("%s", string);


    return 0;
}
