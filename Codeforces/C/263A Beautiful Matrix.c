//0 0 0 0 0
//0 0 0 0 0
//0 0 0 0 0
//0 1 0 0 0
//0 0 0 0 0

//For copying

#include<stdio.h>

int main()
{
    int i, j, breakflag = 0, sum = 0;
    int matrix[5][5];
    for (i = 0; i < 5; i++)
    {
        for (j = 0; j < 5; j++)
        {
            scanf("%d", &matrix[i][j]);
        }
    }

    for (i = 0; i < 5; i++)
    {
        for (j = 0; j < 5; j++)
        {
            if (matrix[i][j] == 1)
            {
//                printf("%d\t%d\n", i, j);
                breakflag = 1;
                break;
            }

        }
        if (breakflag ==1)
        {
            break;
        }
    }



    i = i + 1;
    j = j + 1;


    if (i < 3)
    {
        sum = 3 - i;
    }
    else if (i > 3)
    {
        sum = i - 3;
    }
//    printf("%d\n", sum);

    if (j < 3)
    {
        sum = sum + 3 - j;
    }
    else if (j > 3)
    {
        sum = sum + j - 3;
    }

    printf("%d", sum);




    return 0;
}
