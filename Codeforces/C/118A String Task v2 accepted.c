#include<stdio.h>
#include<string.h>
#include<ctype.h>

int main()
{
    char s[101];
    scanf("%s",s);
    int i;
    for(i=0;s[i];i++)
    {
        s[i]=tolower(s[i]);
    }
    for(i=0;s[i];i++)
    {
        if(s[i]=='a' || s[i]=='e' || s[i]=='i' || s[i]=='o' || s[i]=='u' || s[i]=='y')
            continue;
        else
            printf(".%c",s[i]);
    }
    return 0;
}
