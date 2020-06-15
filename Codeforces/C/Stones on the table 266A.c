#include<stdio.h>


int main()
{
    int n, stringlength, rcount=0, extra_r=0, bcount=0, extra_b=0, gcount=0, extra_g=0, i;
    char string[51];
    scanf("%d", &n);
    scanf("%s", string);

    for (i = 0; i < n; i++)
    {
        if (string[i] == 'R')
        {
            bcount = 0;
            gcount = 0;
            if (rcount == 0)
            {
                rcount++;
            }
            else if (rcount > 0)
            {
                extra_r++;
                rcount++;
            }
//            else if (string[i] == 'B' || string[i] == 'G')
//            {
//                rcount = 0;
//            }

        }



        else if (string[i] == 'B')
        {
            rcount = 0;
            gcount = 0;
            if (bcount == 0)
            {
                bcount++;
            }
            else if (bcount > 0)
            {
                extra_b++;
                bcount++;
            }
//            else if (string[i] == 'R' || string[i] == 'G')
//            {
//                bcount = 0;
//            }
        }


        else if (string[i] == 'G')
        {
            rcount = 0;
            bcount = 0;
            if (gcount == 0)
            {
                gcount++;
            }
            else if (gcount > 0)
            {
                extra_g++;
                gcount++;
            }
//            else if (string[i] == 'B' || string[i] == 'R')
//            {
//                gcount = 0;
//            }
        }


    }

    printf("%d", extra_r + extra_b + extra_g);

    return 0;
}
