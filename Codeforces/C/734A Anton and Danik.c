#include<stdio.h>

int main()
{
    int n,i,countA=0,countD=0;
    scanf("%d",&n);
    char a[n+1];
    for(i=0; i<n+1; i++)//I don't know why i needed to "i<n+1" instead of "i<n"
    {
        scanf("%c",&a[i]);
        if(a[i]=='A')
            countA++;
        else if(a[i]=='D')
            countD++;

    }
//    printf("Anton: %d\tDanik: %d\n",countA,countD);
    if( countA>countD )
        printf("Anton");
    else if( countA<countD )
        printf("Danik");
    else
        printf("Friendship");




    return 0;
}
