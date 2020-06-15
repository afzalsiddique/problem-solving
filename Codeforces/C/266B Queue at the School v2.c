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
        for (j = 1; j < n; )
        {
            if (string[i] < string[j])
            {
                store = string[i];
                string[i] = string[j];
                string[j] = store;
                i+=2;
                j+=2;
            }
            else
            {
                i++;
                j++;
            }
        }
        i = istore;
    }

    printf("%s", string);


    return 0;
}
