#include <bits/stdc++.h>
using namespace std;

#define lli long long int
#define vi vector<int>
#define forn for(int i=0; i<n; i++)
#define form for(int j=0; j<m; j++)
#define forj for(int j=0; j<n; j++)
#define sortn sort(a, a+n);
#define sortb sort(s.begin(), s.end())
#define reversen reverse(a, a+n)
#define reverseb reverse(s.begin(), s.end())
#define pi 2*acos(0.0)
#define MOD 1000000007
#define nln cout<<endl
#define eps 1e-9

typedef long long   LL;

const int MAX_CHARS = 256;

bool is_prime(int n) {int root= sqrt(n); if(n==1) return false; for(int i=2; i<=root; i++){ if(n%i==0) return false;} return true; }
int digitsOfFact(int n) { double x=0; for(int i=1; i<=n; i++){ x+= log10(i);} int res = x + 1 + eps; return res; }
int lcm(LL a,LL b) { LL lar = max(a, b); LL small = min(a, b); for (LL i = lar; ; i += lar){if (i % small == 0) return i;} }
int gcd(LL a,LL b) { if (b == 0) return a; return gcd(b, a % b); }

int main()
{
    int t, n;
    cin>>t;
    while(t--)
    {
        cin>>n;
        //int a[n];

        for(int i=0; i<n; i++)
        cout<<1<<" ";
        cout<<endl;
    }

}