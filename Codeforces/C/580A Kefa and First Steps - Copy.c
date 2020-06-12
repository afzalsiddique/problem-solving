#include<stdio.h>

int main()
{
    int n, i, j, temp1=0, temp2=0, counter=0;
    scanf("%d", &n);
    int input[n+1];

    for(i = 0; i<n; i++)
    {
        scanf("%d", &input[i]);
    }

    for(i=0; i<n; i++)
    {
        if(input[j]>=input[i])
        {
            temp1++;
        }
        else
        {
            if(temp1>counter)
            {
                counter=temp1+1;
                temp1=0;
            }
            else if(temp1<counter)
                temp1=0;
        }
    }
    printf("%d", counter);


    return 0;
}
