#include<stdio.h>
#include<string.h>
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
    else
        return -1;
    return num;
}


int main()
{
    char str[1001];
    int i,count[27]={0},slen,count_unique=0;
    gets(str);
    slen=strlen(str);
    if(slen==2)
        count_unique=0;
    else if(slen==3)
        count_unique=1;
    else
    {
        for(i=1; i<slen; i+=3)
        {
            count[alphabet_to_num(str[i])]++;
        }
    }

    for(i=0; i<26; i++)
    {
        if(count[i])
            count_unique++;
    }

    printf("%d\n",count_unique);
    return 0;
}
