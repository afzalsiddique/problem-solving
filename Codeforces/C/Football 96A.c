#include<stdio.h>
#include<string.h>

int main()
{
    int i, zerocounter = 0, onecounter = 0, stringlen, flag = 0;
    char string[101];
    scanf("%s", string);
    stringlen = strlen(string);

    for (i = 0; i < stringlen; i++)
    {
        if (string[i] == '0')
        {
            zerocounter++;
            if (zerocounter == 7)
            {
                flag = 1;
                break;
            }
            onecounter = 0;
        }
        else if (string[i] == '1')
        {
            onecounter++;
            if (onecounter == 7)
            {
                flag = 1;
                break;
            }
            zerocounter = 0;
        }
    }

    if (flag == 1)
    {
        printf("YES");
    }
    else
    {
        printf("NO");
    }

    return 0;
}
