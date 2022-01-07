#include <bits/stdc++.h>
using namespace std;

int main()
{
    int a,b;
    int c=0;
    while(scanf("%d %d", &a, &b)!=EOF)
        {
            c = a^b;
            cout<<c<<endl;
        }

    return 0;
}
