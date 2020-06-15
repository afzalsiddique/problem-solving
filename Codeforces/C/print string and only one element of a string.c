#include<stdio.h>
#include<string.h>

int main()
{
    char first[101], second[101];
    int i, stringlen1, stringlen2;
    scanf("%s", first);
    scanf("%s", second);
    stringlen1 = strlen(first);
    stringlen2 = strlen(second);

//    printf("%d\n%d\n", stringlen1, stringlen2);
//    printf("%c", first[1]);

    for (i = 0; i < stringlen1; i++)
    {
        if (first[i] >= 'A' && first[i] <= 'Z')
        {
            first[i] = first[i] + ('a' - 'A');
        }
    }

    for (i = 0; i < stringlen2; i++)
    {
        if (second[i] >= 'A' && second[i] <= 'Z')
        {
            second[i] = second[i] + ('a' - 'A');
        }
    }


//    printf("\n%s", first);
//    printf("\n%s", second);

    for (i = 0; ; i++)
    {
        if (first[i] == second[i])
        {
            if (i == stringlen1 - 1)
            {
                printf("%d", 0);
                break;
            }
            else
            {
                continue;
            }
        }
        else if (first[i] < second[i])
        {
            printf("%d", -1);
            break;
        }
        else if (first[i] > second[i])
        {
            printf("%d", 1);
            break;
        }


    }



    return 0;
}
