#include<stdio.h>
#include<string.h>

int main()
{
    char s[101];
    char t[101];
    scanf("%s", s);
    scanf("%s", t);
    int i, j, stringlen, flag = 1;
    stringlen = strlen(s);
    j = stringlen - 1;
//    printf("%d\n", stringlen);

    for (i = 0; i < stringlen; i++)
    {
        for ( ; j >= 0;)
        {
//            printf("%c \t %c\n", s[i], t[j]);
            if (s[i] == t[j])
            {
                j--;
                break;
            }
            else if (s[i] != t[j])
            {
                flag = 0;
                j--;
                break;
            }
        }
        if (flag == 0)
        {
            break;
        }
    }

    if (flag == 0)
        printf("NO");
    else
        printf("YES");



    return 0;
}
