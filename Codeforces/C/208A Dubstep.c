#include<stdio.h>
#include<string.h>

int main()
{
    int i, j, k, slength;
//    int count=0;
    char song[201];
    scanf("%s", song);
    slength = strlen(song);
//    char WUB[4] = "WUB";
//    char original[201];

    for(i=0; i<slength-2; i++)
    {
        if(song[i]=='W' && song[i+1]=='U' && song[i+2]=='B')
        {
            song[i]=' ';
            song[i+1]=' ';
            song[i+2]=' ';
        }
    }
    printf("%s\n", song);
//    for(i=0, j=0, k=0; i<slength; i++)
//    {
//        if(song[i]==' ')
//        {
//            original[k]=' ';
//            k++;
//            for(j=i+1; ; j++)
//            {
//                if (song[j]==' ')
//                {
//                    count++;
//                }
//                else if (song[j]!=' ')
//                {
//                    i+=count;
//                    count=0;
//                }
//            }
//        }
//        else
//        {
//            original[k] = song[i];
//            k++;
//        }
//
//    }
//        printf("%s\n", original);
//
//
//


    return 0;
}
