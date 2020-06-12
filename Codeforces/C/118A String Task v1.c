#include<stdio.h>
#include<string.h>

int main()
{
    char string[101], newstring[101];
    int i, j=0, stringlength;

//    for (i = 0; i < 101; i++)
//    {
        scanf("%s", string);
//    }

    stringlength = strlen(string);
//    printf("%d", stringlength);

    for (i = 0; i < stringlength; i++)
    {
        if (string[i] >= 'a' && string[i] <= 'z' && (string[i] != 'a' && string[i] != 'e' && string[i] != 'i' && string[i] != 'o' && string[i] != 'u' && string[i] != 'y'))
        {
            newstring[j] = '.' ;
            j++;
            newstring[j] = string[i];
            j++;
        }
        else if (string[i] >= 'A' && string[i] <= 'Z' && (string[i] != 'A' && string[i] != 'E' && string[i] != 'I' && string[i] != 'O' && string[i] != 'U' && string[i] != 'Y'))
        {
            newstring[j] = '.' ;
            j++;
            newstring[j] = string[i] - ('A' - 'a');
            j++;
        }
    }

//    for (i = 0; newstring[i] != '\0'; i++)
//    {
//        printf("%c", newstring[i]);
//    }


        printf("%s", newstring);

    return 0;
}
