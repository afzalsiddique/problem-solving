#include<stdio.h>

int cubes_in_line_i(int i)
{
    int sum=0,j;
    for(j=1;j<=i;j++)
    {
        sum+=j;
    }
    return sum;
}

int main()
{
    int i,n,count=0;
    scanf("%d",&n);
    for(i=1;;i++)
    {
        if( n>=cubes_in_line_i(i) )
        {
            n=n-cubes_in_line_i(i);
            count++;
        }
        else
            break;
    }
    printf("%d",count);


    return 0;
}
