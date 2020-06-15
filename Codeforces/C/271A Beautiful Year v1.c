#include<stdio.h>

int main()
{
    int y, diff, mod, ystore, i, j, k, flag = 1;
    int digit[5];
    scanf("%d", &y);
//    diff = 9000 - y;
    ystore = y;

    for ( ; y < 9001; y++)
    {
        ystore = y;

        for (k = 0; k < 4; k++)
        {
            digit[i] = ystore % 10;

//        printf("%d\t", digit[i]);
            ystore = ystore / 10;
        }

        for (i = 0; i < 4; i++)
        {
            for (j = i+1; j < 4; j++)
            {
                if (digit[i] == digit[j])
                {
                    flag = 0;
                    break;
                }
            }
            if (flag == 0)
            {
                break;
            }
        }
    }

    printf("%d", y);



    return 0;
}
