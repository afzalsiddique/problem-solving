#include<stdio.h>

int main()
{
    int a1,a2,a3,b1,b2,b3,n,shelvec,shelvem;
    scanf("%d %d %d",&a1,&a2,&a3);
    scanf("%d %d %d",&b1,&b2,&b3);
    scanf("%d",&n);
    if((a1+a2+a3)%5)
        shelvec=(a1+a2+a3)/5+1;
    else
        shelvec=(a1+a2+a3)/5;

    if((b1+b2+b3)%10)
        shelvem=(b1+b2+b3)/10+1;
    else
        shelvem=(b1+b2+b3)/10;
//    printf("shelvec: %d\tshelvem: %d\n",shelvec,shelvem);

    if(  (shelvec+shelvem)<=n  )
        printf("YES");
    else
        printf("NO");


    return 0;
}
