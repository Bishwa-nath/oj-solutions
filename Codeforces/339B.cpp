#include <bits/stdc++.h>
using namespace std;

#define lli long long int
#define forn for(int i=0; i<n; i++)
#define form for(int i=0; i<m; i++)
#define forj for(int j=0; j<n; j++)
#define PI 3.141592653589793
#define MOD 1000000007
#define sorta sort(a, a+n)
//#define mx max(a, b)
//#define mn min(a, b)

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
    int n, m;
    cin>>n>>m;
    lli ans=0;
    int x=1;

    for(int i=0; i<m; i++){
        int a;
        cin>>a;
        if(x<=a) ans+= a-x;
        else ans += n+a-x;
        x = a;
    }
    cout<<ans<<endl;


    return 0;
}