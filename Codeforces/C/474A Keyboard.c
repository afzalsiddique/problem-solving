#include<stdio.h>

int main()
{
    char row1[11]= {"qwertyuiop"},row2[11]= {"asdfghjkl;"},row3[11]= {"zxcvbnm,./"};
    char choice;
    fflush(stdin);
    scanf("%c",&choice);
    int i;
    char msg[101];
    scanf("%s",msg);
//    gets(msg);
    char *p=msg;
    while(*p)
    {
        for(i=0; i<10; i++)
        {
            if(row1[i]==*p)
            {
                if(choice=='L')
                    printf("%c",row1[i+1]);
                else
                    printf("%c",row1[i-1]);
            }
            else if(row2[i]==*p)
            {
                if(choice=='L')
                    printf("%c",row2[i+1]);
                else
                    printf("%c",row2[i-1]);
            }
            else if(row3[i]==*p)
            {
                if(choice=='L')
                    printf("%c",row3[i+1]);
                else
                    printf("%c",row3[i-1]);
            }
        }
        p++;

    }


    return 0;
}
