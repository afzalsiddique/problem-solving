#include<stdio.h>
#include<string.h>
int main()
{
    int i,j,slen1,slen2,slen3, flag=1;
    char letter[27]="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int lettercountguesthost[27], lettercountpile[27];
    for(i=0; i<26; i++){
        lettercountguesthost[i]=0;
        lettercountpile[i]=0;
    }
    char name1[101], name2[101], name3[101];
    scanf("%s%s%s", name1, name2, name3);
    slen1=strlen(name1);
    slen2=strlen(name2);
    slen3=strlen(name3);
    for(i=0; i<26; i++){
        for(j=0; j<slen1; j++){
            if(letter[i] == name1[j]){
                lettercountguesthost[i]++;
            }
        }
//        printf("letter: %c\t count: %d\n", letter[i], lettercountguesthost[i]);
    }
    for(i=0; i<26; i++){
        for(j=0; j<slen2; j++){
            if(letter[i] == name2[j]){
                lettercountguesthost[i]++;
            }
        }
//        printf("letter: %c\t count: %d\n", letter[i], lettercountguesthost[i]);
    }
    for(i=0; i<26; i++){
        for(j=0; j<slen3; j++){
            if(letter[i] == name3[j]){
                lettercountpile[i]++;
            }
        }
//        printf("letter: %c\t count: %d\n", letter[i], lettercountpile[i]);
    }
    for(i=0; i<26; i++){
        if(lettercountguesthost[i]!=lettercountpile[i]){
            flag=0;
            break;
        }

    }
    if(flag)
        printf("YES");
    else
        printf("NO");

    return 0;
}
