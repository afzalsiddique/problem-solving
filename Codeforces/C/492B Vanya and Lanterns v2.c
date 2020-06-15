#include<stdio.h>

int main()
{
    int n, i, j;
    double highest=-0.0, temp=1.0;
    double l, store;
    scanf("%d %ld", &n,&l);
    double light[n+1];
    for(i=0; i<n; i++)
        scanf("%ld", &light[i]);
    for(i=0; i<n; i++)
    {
        for(j=i+1; j<n; j++)
        {
            if(light[i]>light[j])
            {
                store=light[i];
                light[i]=light[j];
                light[j]=store;
            }
        }
    }
//    for(i=0; i<n; i++)
//        printf("%ld\t", light[i]);
    for(i=0; i<n-1; i++)
    {
        if(i==0)
        {
            if(light[0]!=0){
            temp = light[i] * 2.0;
            printf("0\ti: %d\ttemp: %lf\n", temp);
            //initially setting it double so that when it gets divided by 2 it is adjusted
            }
        }
        else if( i==(n-2) )
        {
            if(light[n-1] != l){
            temp = ( l - light[i+1] ) * 2.0;
            printf("n-2\ti: %d\ttemp: %lf\n", temp);
            //initially setting it double so that when it gets divided by 2 it is adjusted
            }
        }
        else
        {
            temp = light[i+1]-light[i];
            printf("1\ti: %d\ttemp: %lf\n", temp);
        }
        if (temp>highest){
            highest=temp;
        }
        printf("i: %d\ttemp: %lf\n", temp);
    }
    printf("%.12lf", highest/2.0);//multiplication by two got adjusted here
    return 0;
}
