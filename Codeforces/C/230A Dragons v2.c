#include<stdio.h>

int main()
{
    int s,n,i,j,store,count=0;
    scanf("%d%d", &s, &n);
    int x[n+2];
    int y[n+2];
    for(i=0; i<n; i++)
    {
        scanf("%d%d", &x[i], &y[i]);
    }
//    for(i=0; i<n; i++){
//        for(j=i+1; j<n; j++){
//            if(x[i]>x[j]) {
//                store=x[i];
//                x[i]=x[j];
//                x[j]=store;
//            }
//        }
//    }
    for(i=0; i<n; i++)
    {
        for(j=i+1; j<n; j++)
        {
            if(y[i]<y[j])
            {
                store=y[i];
                y[i]=y[j];
                y[j]=store;

                store=x[i];
                x[i]=x[j];
                x[j]=store;
            }
            else if(y[i]==y[j])
            {
                if(x[i]>x[j])
                {
                    store=x[i];
                    x[i]=x[j];
                    x[j]=store;
                }
            }
        }
    }
//comment the following lines
//    for(i=0; i<n; i++)
//    {
//        printf("%d\t%d\n", x[i], y[i]);
//    }
//
    for(i=0; i<n; i++)
    {
        for(j=0; j<n; j++)
        {
            if(x[j]<s)
            {
                s+=y[j];
                count++;
//                printf("j: %d\tcount: %d\n", j, count);
                x[j]=10001;//made it out of range
                y[j]=10001;
                break;
            }
        }
    }
//    printf("%d\n", count);
    if(count==n)
    {
        printf("YES");
    }
    else
        printf("NO");


    return 0;
}
