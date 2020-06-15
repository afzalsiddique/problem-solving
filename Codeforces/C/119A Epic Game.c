#include<stdio.h>

int findgcd(int n1, int n2)
{
    int i,gcd;
    for(i=1;i<=n1 && i<=n2;++i)
        if(n1%i==0 && n2%i==0)
            gcd=i;
    return gcd;

}

int main()
{
    int a,b,n,flag=1;
    scanf("%d%d%d",&a,&b,&n);
    while(n!=0)
    {
        if(flag)
        {
            n=n-findgcd(n,a);
            flag=0;
        }
        else if(!flag)
        {
            n=n-findgcd(n,b);
            flag=1;
        }

    }
    printf("%d",flag);




    return 0;
}
