#include<stdio.h>

int main()
{
    int n, i, counter=1, temp=1, temp2=0, onlyincreasing=1;
    scanf("%d", &n);
    int a[n+1];

    for(i=0; i<n; i++)
    {
        scanf("%d", &a[i]);
    }

    for(i=0; i<n-1; i++)
    {
        if(a[i+1]>=a[i])
        {
            counter++;
        }
        else
        {
            if(temp<=counter)
            {
                temp=counter;
            }
            counter=1;
//            temp=counter;
//            counter=1;
//            onlyincreasing=0;

        }


    }

    if (onlyincreasing)
    {
        printf("%d", counter);
    }
    else if (!onlyincreasing)
    {
        printf("%d", temp);
    }
    else if(temp==1)
        printf("%d", 0);

    return 0;
}
