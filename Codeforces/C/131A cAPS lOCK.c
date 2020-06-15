#include<stdio.h>
#include<string.h>

int main()
{
    char word[101];
    int i, stringlen, flag = 1;
    scanf("%s", word);
    stringlen = strlen(word);



    for (i = 1; i < stringlen; i++) //first letter doesn't matter. that's why i=1;
    {
        if (word[i] >= 'A' && word[i] <= 'Z')
        {
            continue;
        }
        else
        {
            flag = 0; //flag=0 means it doesn't meet the conditions
        }
    }

//    printf("%d", flag);

    if (flag == 1)
    {
        for (i = 0; i < stringlen; i++)
        {
            if (word[i] >= 'A' && word[i] <= 'Z')
            {
                word[i] = word[i] + ('a' - 'A');
            }
            else if (word[i] >= 'a' && word[i] <= 'z')
            {
                word[i] = word[i] - ('a' - 'A');
            }
        }

        printf("%s", word);
    }
    else
    {
        printf("%s", word);
    }


    return 0;
}
