#include<stdio.h>

//int minimum(int n)
//{
//    int i,min=101,temp;
//    for(i=0;i<n;i++)
//    {
//        scanf("%d",&temp);
//        if(temp<min)
//            min=temp;
//    }
//    return min;
//}
//int maximum(int n)
//{
//    int i,max=-1,temp;
//    for(i=0;i<n;i++)
//    {
//        scanf("%d",&temp);
//        if(temp<min)
//            max=temp;
//    }
//    return max;
//}

int main()
{
    int n,i,min=101,max=-1;
    int posmin;//position of min from "RIGHT" side
    int posmax;//position of max from "LEFT" side
    scanf("%d",&n);
    int a[n+1];
    for(i=0; i<n; i++)
    {
        scanf("%d",&a[i]);
        if(a[i]<min)
        {
            min=a[i];
        }
        else if(a[i]>max)
        {
            max=a[i];
        }
    }
//    printf("max: %d\tmin: %d\n",max,min);

//position of max from "LEFT" side
    for(i=0; i<n; i++)
    {
        if(a[i]==max)
        {
            posmax=i;
            break;
        }
    }

//position of min from "RIGHT" side
    for(i=n-1; i>=0; i--)
    {
        if(a[i]==min)
        {
            posmin=i;
            break;
        }
    }
    printf("posmax: %d\tposmin: %d\n",posmax,posmin);

    if(posmax==0 && posmin==n-1)
    {
        printf("%d",0);
    }
    else if(posmax>posmin)
    {
        printf("%d",posmax+(n-1)-posmin-1);
    }
    else
        printf("%d",posmax+(n-1)-posmin);


    return 0;
}
