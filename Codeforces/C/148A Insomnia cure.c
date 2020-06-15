#include<stdio.h>

int main()
{
    int k,l,m,n,d,i,kmul,lmul,mmul,nmul, count=0;
    //kmul implies multioles of k
    scanf("%d%d%d%d%d", &k,&l,&m,&n,&d);
    int dragon[d+2];
    dragon[0]=99;
    for(i=1; i<d+1; i++)
        dragon[i]=1;
//    for(i=0; i<d+1; i++)
//        printf("%d ", dragon[i]);
//    printf("\n");

    for(i=1,kmul=k; kmul<d+1; kmul=k*i)
    {
//        printf("i: %d\tkmul: %d\n", i, kmul);
        dragon[kmul]=0;
        i++;
    }

    for(i=1,lmul=l; lmul<d+1; lmul=l*i)
    {
//        printf("i: %d\tlmul: %d\n", i, lmul);
        dragon[lmul]=0;
        i++;
    }
    for(i=1,mmul=m; mmul<d+1; mmul=m*i)
    {
//        printf("i: %d\tmmul: %d\n", i, mmul);
        dragon[mmul]=0;
        i++;
    }

    for(i=1,nmul=n; nmul<d+1; nmul=n*i)
    {
//        printf("i: %d\tnmul: %d\n", i, nmul);
        dragon[nmul]=0;
        i++;
    }

    for(i=1;i<d+1;i++)
    {
        if(dragon[i]==0)
            count++;
    }
    printf("%d", count);

//    for(i=0; i<d+1; i++)
//        printf("%d ", dragon[i]);
//    printf("\n");


    return 0;
}
