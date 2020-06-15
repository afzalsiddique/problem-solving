#include<stdio.h>

int main()
{
    int n, i, j, no_taxi=0, count1=0, count2=0, count3=0, count4=0;
    int num[100002];
    scanf("%d", &n);

    for (i = 0; i < n; i++)
    {
        scanf("%d", &num[i]);
    }


    for (i = 0; i < n; i++)
    {
        if (num[i] == 1)
        {
            count1++;
        }
        else if (num[i] == 2)
        {
            count2++;
        }
        else if (num[i] == 3)
        {
            count3++;
        }
        else if (num[i] == 4)
        {
            count4++;
        }
    }
//    printf("%d\t%d\t%d\t%d\n", count1, count2, count3, count4);

    if ( count2%2 == 0)
    {
        if (count3<count1)
        {
            count1 -= count3;
            if (count1 % 4 == 0)
            {
                no_taxi = count4 + count3 + (count1/4) + (count2/2);
            }
            else if (count1 % 4 != 0)
            {
                no_taxi = count4 + count3 + (count1/4) + (count2/2)+1;
            }
//            printf("%d", count1);
        }
        else if(count3 >= count1)
        {
            no_taxi = count4 + count3 + (count2/2);
//            printf("%d", count1);
        }
    }


    else if ( count2%2 != 0)
    {
        if (count3<count1)
        {
            count1 -= count3;
            if (count1%4 < 3)
            {
                no_taxi = count4 + count3 + (count2/2) + (count1/4) + 1;
            }
            else if (count1%4 > 3)
            {
                no_taxi = count4 + count3 + (count2/2) + (count1/4) + 2;
            }
            else if (count1%4 == 3)
            {
                no_taxi = count4 + count3 + (count2/2) + (count1/4);
            }

        }
        else if(count3 >= count1)
        {
            no_taxi = count3 + (count2/2)+1 + count4;
        }
    }

    printf("%d", no_taxi);





    return 0;
}
