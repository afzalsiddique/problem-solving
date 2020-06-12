#include<stdio.h>
#include<math.h>

int findlog2(long long a)
{
    double ans;
    int answer;
    ans= log10(a)/log10(2);
    answer=(int)ans;
    return answer;
}

//int main()
//{
//    long x;
//    scanf("%ld", &x);
//    printf("%d", findlog2(x));
//}


int main()
{
    long long x,result;
    scanf("%lld",&x);
    int i,flageven=1,count=0,ans;
    if(x%2)
    {
        flageven=0;
        x--;
    }

    for(; x!=0;)
    {
        ans = findlog2(x);
//        ans = (int)ans;
        result=pow(2,ans);
//        printf("ans: %d\tresult: %ld\t count: %d\tx: %ld\n", ans,result,count,x);
        x=x-result;
        count++;
    }
//    if(x==1)
//    {
//        printf("%d",1);
//    }
    if(flageven)
    printf("%d", count);
    else
        printf("%d",count+1);


    return 0;
}
