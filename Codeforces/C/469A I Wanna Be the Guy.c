#include<stdio.h>

int main()
{
    int n,p,q,i,j,level[202],temp,zerocount=0;
    scanf("%d",&n);
    int count[n+1];
    scanf("%d",&p);
    for(i=0; i<p; i++)
    {
        scanf("%d",&level[i]);
    }
    scanf("%d",&q);
    for(j=0; j<q;i++,j++)
    {
        scanf("%d",&level[i]);

    }


    //sorting
    for(i=0;i<p+q;i++)
    {
        for(j=i+1;j<p+q;j++)
        {
            if(level[i]>level[j])
            {
                temp=level[i];
                level[i]=level[j];
                level[j]=temp;
            }
        }
    }


//    for(i=0;i<p+q;i++)
//    {
//        printf("%d\t",level[i]);
//    }
//    printf("\n");

//making same zerps
    for(i=0;i<p+q;i++)
    {
        for(j=i+1;j<p+q;j++)
        {
            if(level[i]==level[j])
            {
                level[i]=0;
                zerocount++;
            }
        }
    }

    if(n==(p+q)-zerocount)
        printf("I become the guy.\n");
    else
        printf("Oh, my keyboard!\n");


//    for(i=0;i<p+q;i++)
//    {
//        printf("%d\t",level[i]);
//    }
//    printf("\n");
//
////again sorting
//    for(i=0;i<p+q;i++)
//    {
//        for(j=i+1;j<p+q;j++)
//        {
//            if(level[i]>level[j])
//            {
//                temp=level[i];
//                level[i]=level[j];
//                level[j]=temp;
//            }
//        }
//    }
//
//
//    for(i=0;i<p+q;i++)
//    {
//        printf("%d\t",level[i]);
//    }
//    printf("\n");
//
////eliminating all the zeros
//    for(i=0;i<(p+q)-zerocount;i++)
//        level[i]=level[i+zerocount];
//    level[i]='\0';
//
//    for(i=0;i<(p+q)-zerocount;i++)
//    {
//        printf("%d\t",level[i]);
//    }
//    printf("\n");

    return 0;
}
