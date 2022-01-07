#include <bits/stdc++.h>
using namespace std;

#define rapid   ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define in_out  freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);
#define lli     long long int
#define forn    for(int i=0; i<n; i++)
#define form    for(int i=0; i<m; i++)
#define forj    for(int j=0; j<n; j++)
#define PI      3.141592653589793
#define MOD     1000000007
#define nln     cout<<"\n"
#define eps     1e-9

typedef long long   LL;
const int MAX_CHARS = 256;

bool is_prime(int n) {int root= sqrt(n); if(n==1) return false; for(int i=2; i<=root; i++){ if(n%i==0) return false;} return true; }
bool is_palindrome(string s){ return equal(s.begin(), s.begin() + s.size()/2, s.rbegin()); }
int digitsOfFact(int n) { double x=0; for(int i=1; i<=n; i++){ x+= log10(i);} int res = x + 1 + eps; return res; }
int lcm(LL a,LL b) { LL lar = max(a, b); LL small = min(a, b); for (LL i = lar; ; i += lar){if (i % small == 0) return i;} }
int gcd(LL a,LL b) { if (b == 0) return a; return gcd(b, a % b); }
int Fact(int n){ if(n==0) return 1; return n*Fact(n-1); }
int arr[95];


int main()
{
    int t, n;
    cin>>t;
    while(t--)
    {
        cin>>n;
        for(int i=1; i<=n; i++)
            cout<<i<<" ";
        nln;
    }
    return 0;
}