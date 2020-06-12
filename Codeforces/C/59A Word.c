#include<stdio.h>
#include<string.h>

int main()
{
    int ucount=0,lcount,i,slen;//ucount means uppercase letter count
    char word[101];
    scanf("%s",word);
    slen = strlen(word);

    for(i=0; i<slen; i++)
        if(word[i]>='A' && word[i]<='Z')
            ucount++;
    lcount=slen-ucount;
//    printf("ucount: %d\tlcount: %d\n",ucount,lcount);
    if(lcount>=ucount)
    {
        for(i=0; i<slen; i++)
        {
            if(word[i]>='A' && word[i]<='Z')
            {
                word[i] = 'a' + (word[i]-'A');
            }
        }
    }
    else
    {
        for(i=0; i<slen; i++)
        {
            if(word[i]>='a' && word[i]<='z')
            {
                word[i] = 'A' + (word[i]-'a');
            }
        }
    }
    printf("%s",word);

    return 0;
}

//        if (country [i] >= 'a' && country [i] <= 'z') {
//            country [i] = 'A' + (country [i] - 'a');
//        }
