#include <iostream>

using namespace std;

int main(){

    int a;
    int t;
    cin>>t;

    while(t--)
    {
        cin>>a;

        if(360 % (180-a)==0)
        {
            cout<<"YES"<<endl;
        }

        else
        {
            cout<<"NO"<<endl;
        }
    }


    return 0;

}
