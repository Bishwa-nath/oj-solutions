#include <bits/stdc++.h>
using namespace std;

#define lli long long int
#define forn for(int i=0; i<n; i++)
#define form for(int i=0; i<m; i++)
#define forj for(int j=0; j<n; j++)
#define PI 3.141592653589793
#define MOD 1000000007
#define sorta sort(a, a+n)
#define nln cout<<endl

const int N = 51;
int a[N][N];

int SOD ( int n ) {
    int sqrtn = sqrt ( n );
    int res = 0;
    for ( int i = 1; i < sqrtn; i++ ) {
        if ( n % i == 0 ) {
            res += i; 
            res += n / i; 
        }
    }
    if ( n % sqrtn == 0 ) {
        if ( sqrtn * sqrtn == n ) res += sqrtn;
        else {
            res += sqrtn; 
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
        int n;
        cin>>n;
        int a[n];
        forn cin>>a[i];

        if(a[0] < a[n-1]) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }

    return 0;
}