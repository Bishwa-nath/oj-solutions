#include <bits/stdc++.h>
using namespace std;

#define lli long long int
#define forn for(int i=0; i<n; i++)
#define form for(int i=0; i<m; i++)
#define forj for(int j=0; j<n; j++)
#define PI 3.141592653589793
#define MOD 1000000007
#define sorta sort(a, a+n)
#define mx max(a, b)
//#define mn min(a, b)
#define nln cout<<endl

const int N = 51;
int a[N][N];

int SOD ( int n ) {
    int sqrtn = sqrt ( n );
    int res = 0;
    for ( int i = 1; i < sqrtn; i++ ) {
        if ( n % i == 0 ) {
            res += i; //"i" is a divisor
            res += n / i; //"n/i" is also a divisor
        }
    }
    if ( n % sqrtn == 0 ) {
        if ( sqrtn * sqrtn == n ) res += sqrtn; //Perfect Square.
        else {
            res += sqrtn; //Two different divisor
            res += n / sqrtn;
        }
    }
    return res;
}

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n, x;
        cin>>n;
        int a[n], b[n];
        forn{
            cin>>x;
            if(x<0) x*=(-1);
            a[i] = x;
        }
        for(int i=1; i<n; i+=2)
            a[i] = a[i]*(-1);

        forn
        cout<<a[i]<<' ';
        cout<<endl;

    }

    return 0;
}