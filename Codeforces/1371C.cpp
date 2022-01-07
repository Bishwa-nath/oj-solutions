#include <bits/stdc++.h>
using namespace std;

#define lli long long int
#define forn for(int i=0; i<n; i++)
#define form for(int i=0; i<m; i++)
#define forj for(int j=0; j<n; j++)
#define PI 3.141592653589793
#define MOD 1000000007
#define sorta sort(a, a+n)

int main()
{
    int t;
    cin>>t;

    while(t--)
    {
        lli a, b, n, m;
        lli x, y;
        cin>>a>>b>>n>>m;
        lli  mn = min(a, b);

        x = a+b;
        y = m+n;

        if(m> mn || y > x) cout<<"No\n";
        else cout<<"Yes\n";
    }
    return 0;
}