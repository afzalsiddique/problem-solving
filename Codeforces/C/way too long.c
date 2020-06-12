#include <stdio.h>
#include <string.h>
//
//

//Problems

//limitations



int main()
{
    int n, len [102];

    char str[102] [102];
    int i, j, a, b;

    scanf("%d", &n);

    for (i = 0; i < n; i ++)
    {
        scanf("%s", str [i]);
        len [i] = strlen(str [i]);
    }

    for (i = 0; i < n; i ++)
    {
        a = len [i];
        if (len [i] > 10)
        {
            a = a - 2;
            printf("%c%d%c", str[i][0], a, str [i][len[i]]);
        }
    }
}
