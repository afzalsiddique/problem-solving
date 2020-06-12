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
    double radius=0.0;
//    printf("Enter the number of lanterns and the length of the road:\n");
    scanf("%d %ld",&n,&l);
    long arr[n+1],*p;
    double arrdiff[n+2];
//    printf("Enter the positions of the lantern:\n");
    for(i=0; i<n; i++)
    {
        scanf("%ld",&arr[i]);
    }
    p=&arr[0];
    ascending_order(n,p);
//    for(i=0; i<n; i++)
//    {
//        printf("%d\t\t",*p);
//        p++;
//    }
//    printf("\n");
    p=arr;
    for(i=0; i<n-1; i++)
    {
        arrdiff[i]= (double)( (arr[i+1]-arr[i])/2.0 );
    }
    arrdiff[i]=(double) ( arr[0] );
    i++;
    arrdiff[i]=(double)(l-arr[n-1]);


//    for(i=0; i<n+1; i++)
//    {
//        printf("%.12lf\t",arrdiff[i]);
//    }
//    printf("\n");

    for(i=0; i<n+1; i++)
    {
        if(arrdiff[i]>radius)
            radius=arrdiff[i];
    }
    printf("%.9lf",radius);

    return 0;
}
