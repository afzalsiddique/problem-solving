#include<stdio.h>
int main(){
    long n;
    int k,i;
    scanf("%ld%d",&n,&k);
    for(i=0;i<k;i++)
        if(n%10)n--;
        else n/=10;
    printf("%ld",n);
    return 0;
}
