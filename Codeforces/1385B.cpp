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
    int n, x;
    cin>>n;
    vector<int> vc;
    int m = n*2;
    int ar[m];
    for(int i=0; i<m; i++) cin>>ar[i];
    unordered_set<int> s(ar, ar+m);

    for(auto x: s)
        vc.push_back(x);

    reverse(vc.begin(), vc.end());

    for(auto x: vc)
        cout<<x<<" ";
    nln;

}

int main()
{
    int t;
    cin>>t;
    while(t--)
        solve();
    return 0;
}