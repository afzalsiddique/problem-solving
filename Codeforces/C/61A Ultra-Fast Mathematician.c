#include<stdio.h>
#include<string.h>
int main()
{
    char a[101],b[101];
    int i,slen;
    scanf("%s%s",a,b);
    slen=strlen(a);
    for(i=0;i<slen;i++)
    {
        if(a[i]==b[i])
            printf("%d",0);
        else
            printf("%d",1);
    }



    return 0;
}
