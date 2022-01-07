#include <bits/stdc++.h>
using namespace std;

#define lli long long int
#define forn for(int i=0; i<n; i++)
#define form for(int i=0; i<m; i++)
#define forj for(int j=0; j<n; j++)
#define PI 3.141592653589793
#define MOD 1000000007
#define sorta sort(a, a+n)

int rev(int n)
{
    int p=0;
    while(n != 0)
    {
        p*=10;
        p += n%10;
        n/=10;
    }
    return p;
}

int main()
{
    int n;
    cin>>n;
    if(n%2)
    cout<<9<<" "<<n-9<<endl;
    else cout<<8<<" "<<n-8<<endl;


    return 0;
}