#include <bits/stdc++.h>
using namespace std;

#define lli long long int
#define forn for(int i=0; i<n; i++)
#define form for(int i=0; i<m; i++)
#define forj for(int j=0; j<n; j++)
#define PI 3.141592653589793
#define nln cout<<endl
#define eps 1e-9

typedef long long   LL;

const int MAX_CHARS = 256;

bool is_prime(int n) {int root= sqrt(n); if(n==1) return false; for(int i=2; i<=root; i++){ if(n%i==0) return false;} return true; }
int digitsOfFact(int n) { double x=0; for(int i=1; i<=n; i++){ x+= log10(i);} int res = x + 1 + eps; return res; }
int lcm(LL a,LL b) { LL lar = max(a, b); LL small = min(a, b); for (LL i = lar; ; i += lar){if (i % small == 0) return i;} }
int gcd(LL a,LL b) { if (b == 0) return a; return gcd(b, a % b); }

bool solve()
{
    int n;
    cin>>n;
    int ar[n];
    forn cin>>ar[i];
    if(n==1) return true;

    for(int i=0; i<n-1; i++)
        for(int j=i+1; j<n; j++)
        {
            int x = abs(ar[i] - ar[j]);
            if(x%2==1) return false;
        }


    return true;
}

int main()
{
    int t;
    cin>>t;
    while(t--)
        if(solve())
            cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    return 0;
}