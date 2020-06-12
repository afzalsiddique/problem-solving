#include<stdio.h>

int main()
{
    int n, i, count1=0, count2=0, count3=0, count4=0;
    int number[100001];
    scanf("%d", &n);

    for (i = 0; i < n; i++)
    {
        scanf("%d", &number[i]);
    }



    for (i = 0; i < n; i++)
    {
        if (number[i] == 1)
        {
            count1++;
        }
        else if (number[i] == 2)
        {
            count2++;
        }
        else if (number[i] == 3)
        {
            count3++;
        }
        else if (number[i] == 4)
        {
            count4++;
        }

    }



//    printf("%d\t%d\t%d\t%d", count1, count2, count3, count4);


    return 0;
}
