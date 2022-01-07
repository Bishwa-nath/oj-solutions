#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long int a, b, t, n, k;
    cin>>t;
    while(t--)
    {
        cin>>n>>k;
        a = (n/k)*k;
        b = n%k;
        a+= min(k/2, b);
        cout<<a<<endl;
    }


    return 0;
}
