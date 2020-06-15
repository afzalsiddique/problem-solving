#include <stdio.h>
#include <string.h>

int main()
{
    int i, j, store, n;
    char str[1002];
    scanf("%s", str);
    n = strlen(str);
//    printf("%d", n);



//    for (i = 0; i < n; i++)
//    {
//        scanf("%d", &str[i]);
//    }

    for (i = 0; i < n; i+=2)
    {
        for (j = i+2; j < n; j+=2)
        {
            if (str[i] > str[j])
            {
                store = str[i];
                str[i] = str[j];
                str[j] = store;
            }
        }
    }

    printf("%s", str);

//    for (i = 0; i<n; i+=2)
//    {
//        printf("%d\n", str[i]);
//    }

    return 0;
}
