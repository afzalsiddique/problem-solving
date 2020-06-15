#include<stdio.h>

int main()
{
    int year, i, temp, digit[5];
    scanf("%d", &year);
    year++;
    for(; ; year++)
    {

        temp=year;
        for(i=0; i<4; i++)
        {
            digit[i]=temp%10;
            temp/=10;
        }
        if (digit[0]!=digit[1 ]&& digit[1]!=digit[2] && digit[2]!=digit[3]
            && digit[0]!= digit[2] && digit[0]!=digit[3] && digit[1]!=digit[3])
        {
            printf("%d", year);
            break;
        }
    }


    return 0;
}
