#include<stdio.h>

int alphtonum(char ch)
{
    int num;
    if(ch>='A' && ch<='Z')
    {
        num = 1+ ch-'A';
    }
    else if(ch>='a' && ch<='z')
    {
        num = 1+ ch-'a';
    }
    return num;
}
int main()
{
    int n,i,count[27],num,flag=1;
    char ch;
    scanf("%d",&n);
    for(i=1;i<=26;i++)
        count[i]=0;
    for(i=1;i<=n;i++)
    {
        scanf("%c",&ch);
        num=alphtonum(ch);
        count[num]++;
    }
    for(i=1;i<=26;i++)
            if(count[i]==0)
            {
                flag=0;
                break;
            }
    if(flag)
        printf("YES");
    else
        printf("NO");

    return 0;
}
