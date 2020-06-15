#include<stdio.h>

int main()
{
    int row,col,i,j;
    scanf("%d%d",&row,&col);
    for(i=1; i<=row; i++)
    {
        for(j=1; j<=col; j++)
        {
            if(i%2)
            {
                printf("#");
            }
            else if(i%2==0 && i%4!=0)
            {
                if(j!=col)
                {
                    printf(".");
                }
                else
                {
                    printf("#");
                }
            }
            else //if(i%4==0)
            {
                if(j!=1)
                {
                    printf(".");
                }
                else
                {
                    printf("#");
                }
            }
        }
        printf("\n");
    }


    return 0;
}
