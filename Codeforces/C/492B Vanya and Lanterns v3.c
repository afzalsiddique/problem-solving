#include<stdio.h>

void ascending_order(int n,long *p)
{
    long temp;
    int i,j;
    for(i=0; i<n; i++)
    {
        for(j=i+1; j<n; j++)
        {
            if(p[i]>p[j])
            {
                temp=p[i];
                p[i]=p[j];
                p[j]=temp;
            }
        }
    }
}


int main()
{
    int n,i;
    long l;
    printf("Enter the number of lanterns:\n");
    scanf("%d",&n);
    printf("Enter the length of the road:\n");
    scanf("%ld",&l);
    long arr[n+1],*p;
    for(i=0;i<n;i++)
    {
        scanf("%ld",&arr[i]);
    }
    p=&arr[0];
    ascending_order(n,p);
    for(i=0;i<n;i++)
    {
        printf("%d\t",*p);
        p++;
    }




    return 0;
}
