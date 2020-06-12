#include<stdio.h>

int main()
{
    long n, m, i, j;
    long long sum=0;
    scanf("%ld%ld", &n, &m);
    int house[m+2];
    for(i=1; i<m+1; i++){
        scanf("%ld", &house[i]);
    }
    //calculating unit from Xenia's house to the 1st house
    i=1;
    sum=house[i]-1;
    for(i=1; i<m; i++){
            if(house[i]>house[i+1]){
                sum = sum + n+house[i+1]-house[i];
            }
            else{
                sum = sum + house[i+1]-house[i];
            }
    }

    printf("%lld", sum);

    return 0;
}
