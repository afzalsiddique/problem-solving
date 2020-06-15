#include<stdio.h>
int main(){
    int n,m,i;
    scanf("%d%d",&n,&m);
    for(i=0,n-=1;n>=0;i++){
        if(i%m)
            n--;
    }
    printf("%d",i-1);
    return 0;
}
