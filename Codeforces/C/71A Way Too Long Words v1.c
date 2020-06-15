#include<stdio.h>
#include<string.h>

int main()
{
    int n,i,length;
    int word[101];
    scanf("%d",&n);
    for(i=0;i<n;i++)
        {
            fflush(stdin);
            scanf("%s",word);
            length=strlen(word);
            printf("%d\n",length);
            if(length<10)
                printf("%s\n",word);
            else
            {
                printf("%c",word[0]);
                printf("%d",length-2);
                printf("%c\n",word[length-2]);
            }
        }



    return 0;
}
