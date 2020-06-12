#include<stdio.h>
#include<string.h>

int main()
{
    char string[101];
    int i, stringlen, flag = 0;
    scanf("%s", string);
    stringlen = strlen(string);

    for (i = 0; i < stringlen; i++)
    {
        if (string[i] =='H' || string[i] =='Q' || string[i] =='9' ||
            (string[i] =='+' && string[i] =='9')
            )
        {
            flag = 1;
            break;
        }
    }

    if (flag == 1)
        printf("YES");
    else
        printf("NO");

    return 0;
}
