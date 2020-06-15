#include<stdio.h>

int main()
{
    int i, n, ans1, ans2, ans3, total = 0, ans_counter = 0; //total = number of people who know the right ans
    scanf("%d", &n);
    for (i = 1; i <= n; i++)
    {
        scanf("%d %d %d", &ans1, &ans2, &ans3);
        total = ans1 + ans2 + ans3;
        if (total > 1)
        {
            ans_counter++;
        }
        total = 0;
    }

    printf("%d", ans_counter);



    return 0;
}
