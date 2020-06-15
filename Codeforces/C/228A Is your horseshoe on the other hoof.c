#include<stdio.h>

int main()
{
    int i=4,j,k,color[5],temp,count=0;
    while(i--)
        scanf("%d",&color[i]);
//    if(color[i]==color[i+1] && color[i]==color[i+2] && color[i]==color[i+3] )
//        count=4;
//    else
    {
        for(k=0; k<3; k++)
        {
            //sorting
            for(i=0; i<4; i++)
            {
                for(j=i+1; j<4; j++)
                {
                    if(color[i]>color[j])
                    {
                        temp=color[i];
                        color[i]=color[j];
                        color[j]=temp;
                    }
                }
            }
            //if same number occurs replacing one of then with zero and counting zeros
            for(i=0; i<3; i++)
            {
                if(color[i]==color[i+1])
                {
                    color[i]=0;
//                    count++;
//                    printf("%d",count);
                }
            }
        }
        for(i=0;i<4;i++)
        {
            if(color[i])
                count++;
        }
//    }
        printf("%d",4-count);

        return 0;
    }
}
