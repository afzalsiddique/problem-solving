#include<stdio.h>

//This function counts the highest non-decreasing sequence in an array

int counting_non_decreasing(int n, long *p);

int main()
{
    int n,count=1;
    scanf("%d",&n);
    long a[n+1],*p;
    for(int i=0; i<n; i++)
    {
        scanf("%d",&a[i]);
    }

    p=a;

    printf("%d",counting_non_decreasing(n,p) );


    return 0;
}

int counting_non_decreasing(int n, long *p)
{
    int max=1,count=1;
    if(n==1)
        return 1;
    else
    {
        for(int i=0; i<n-1; i++,p++)
        {
            if( *(p+1)>=*p )
            {
                count++;
//                if(max<count)
//                    max=count;
//
            }
            else
            {
                count=1;
            }
            if(max<count)
                max=count;
        }
    }
    return max;

}
