#include<stdio.h>
int main(){
    int n,i,j,count=0;
    scanf("%d",&n);
    int home[n+1],away[n+1];
    for(i=0; i<n; i++)
        scanf("%d%d",&home[i],&away[i]);
    for(i=0; i<n; i++)
        for(j=0; j<n; j++)
            if(home[i]==away[j])
                count++;
    printf("%d",count);
    return 0;
}
