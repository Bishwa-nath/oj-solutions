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
    int l, n, t;
    cin>>t;

    while(t--)
    {
        cin>>n;
         l = (n+1)/2;
         cout<<l<<endl;
    }

    return 0;
}