#include<stdio.h>

int main()
{
    int n,t,i,j;
    char queue[51],temp;
    scanf("%d%d",&n,&t);
    scanf("%s",queue);
    for(i=0; i<t; i++)
    {
        for(j=0; j<n-1; )
        {
            if(queue[j]=='B' && queue[j+1]=='G')
            {
                temp=queue[j];
                queue[j]=queue[j+1];
                queue[j+1]=temp;
                j+=2;
            }
            else
                j++;
        }
//        printf("t: %d\t%s\n",i+1,queue);

    }
    printf("%s",queue);



    return 0;
}
