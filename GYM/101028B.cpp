#include<stdio.h>
#include<string.h>

int main()
{
    int t,j;
    scanf("%d",&t);
    int i,slen1,slen2,flag=1;
    for(j=0; j<t; j++)
    {
        char word1[101],word2[101];
        scanf("%s%s",word1,word2);
        slen1=strlen(word1);
        slen2=strlen(word2);
        if(slen1!=slen2)
            printf("No\n");
        else
        {
            for(i=0; i<slen1; i++)
            {
                if(word1[i]>='a' && word1[i]<='z')
                    word1[i]='A' + (word1[i] - 'a');
                if(word2[i]>='a' && word2[i]<='z')
                    word2[i]='A' + (word2[i] - 'a');
            }

            for(i=0; i<slen1; i++)
            {
                if(word1[i]=='P'|| word1[i]=='B')
                    word1[i]='P';
                else if(word1[i]=='E'|| word1[i]=='I')
                    word1[i]='E';
                if(word2[i]=='P'|| word2[i]=='B')
                    word2[i]='P';
                else if(word2[i]=='E'|| word2[i]=='I')
                    word2[i]='E';
            }
//            printf("%s\t%s\n",word1,word2);

            for(i=0; i<slen1; i++)
            {
                if(word1[i]!=word2[i])
                {
                    flag=0;
                    break;
                }
            }
            if(flag)
                printf("Yes\n");
            else
                printf("No\n");
            flag=1;
        }
    }
    return 0;
}
