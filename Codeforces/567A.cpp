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

void solve()
{
    int n;
    cin>>n;
    int ar[n];
    forn cin>>ar[i];
    cout<<abs(ar[0]-ar[1])<<" "<<ar[n-1]-ar[0]<<endl;
    for(int i=1; i<n-1; i++)
    {
        int mn = min(abs(ar[i]-ar[i-1]), abs(ar[i]-ar[i+1]));
        int mx = max(abs(ar[i]-ar[0]), abs(ar[i]-ar[n-1]));
        cout<<mn<<" "<<mx<<endl;
    }
    cout<<ar[n-1]-ar[n-2]<<' '<<ar[n-1]-ar[0]<<endl;
}

int main()
{

    solve();
    return 0;
}