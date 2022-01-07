#include <bits/stdc++.h>
using namespace std;

int main()
{
    int res, a, b, c, d;
    cin>>a>>b>>c>>d;
    while(a>0 && b>0 && c>0 && d>0){

        res = abs(a-c) + abs(b-d);
        cout<<res<<endl;
        cin>>a>>b>>c>>d;
    }

    return 0;
}
