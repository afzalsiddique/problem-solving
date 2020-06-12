#include<stdio.h>

int main()
{
    int n, i, j, count=0;
    scanf("%d", &n);
    int number[n+1];
    for(i=0; i<n; i++)
    {
        scanf("%d", &number[i]);
    }

    for(i=0; i<n; i++){
        if(number[i]%2){
            number[i] = 0;
            count++;
        }
        else{
            number[i] = 1;
        }
    }

    for(i=0; i<n; i++){
        if(count>1){
            if(number[i]==1){
                printf("%d", i+1);
                break;
            }
        }
        else{
            if(number[i]==0){
                printf("%d", i+1);
                break;
            }
        }
    }


    return 0;
}
