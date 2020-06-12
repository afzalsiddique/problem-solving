#include<stdio.h>
#include<string.h>

int main()
{
    int i, j=0, slength, flag=0, counter=0;
    char hello[6] = "hello";
    char input[101];
    scanf("%s", input);
    slength=strlen(input);
//    printf("%d", slength);

    for(i=0; i<slength; i++)
    {
        if (input[i]==hello[j])
        {
            counter++;
            j++;
            if(counter==5)
                break;
        }
    }

    if (counter==5)
        printf("YES");
    else
        printf("NO");




    return 0;
}
