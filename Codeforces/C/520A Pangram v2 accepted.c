#include<stdio.h>
#include <string.h>
char ch[105];
int alphabet_to_num(char ch)
{
    int num;
    if(ch>='A' && ch<='Z')
    {
        num = ch-'A';
    }
    else if(ch>='a' && ch<='z')
    {
        num = ch-'a';
    }
    return num;
}
int main()
{
    int n,i,count[26],flag=1;
    scanf("%d",&n);

    for(i=0;i<26;i++)
        count[i]=0;
    scanf("%s", ch);
    for(i=0;i<strlen(ch);i++)
    {
        count[alphabet_to_num(ch[i])]++;
    }
    /*for(i=0;i<26;i++)
    {
        printf("%c-> %d\n",i+65 ,count[i]);
    }*/
    for(i=0;i<26;i++)
         {
            if(count[i]==0)
            {
                printf("NO");
                return 0;
            }

            else
            {
                flag=1;
            }
         }

    if(flag) printf("YES");



    return 0;
}
