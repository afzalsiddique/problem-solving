#include<stdio.h>
#include<string.h>

int main()
{
    char username[101];
    int letternum[27];
    char abc[27];
    int i, j, stringlen, count=0;
    scanf("%s", username);
    stringlen = strlen(username);


    for(i = 0; i < 26; i++)
    {
        letternum[i] = 0;
        abc[i] = 'a' + i;
    }

//        abc[i] = '\0'; //Still working without this null character



    for (i = 0; i < stringlen; i++)
    {
        for (j = 0; j < 26; j++)
        {
            if (username[i] == abc[j])
            {
                letternum[j] = 1;
            }
        }
    }

    for (j = 0; j < 26; j++)
    {
        count += letternum[j];
    }

    if (count % 2 == 0)
        printf("CHAT WITH HER!");
    else
        printf("IGNORE HIM!");


    return 0;
}
