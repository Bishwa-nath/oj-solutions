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
bool is_palindrome(string s){ return equal(s.begin(), s.begin() + s.size()/2, s.rbegin()); }
int digitsOfFact(int n) { double x=0; for(int i=1; i<=n; i++){ x+= log10(i);} int res = x + 1 + eps; return res; }
int lcm(LL a,LL b) { LL lar = max(a, b); LL small = min(a, b); for (LL i = lar; ; i += lar){if (i % small == 0) return i;} }
int gcd(LL a,LL b) { if (b == 0) return a; return gcd(b, a % b); }
int Fact(int n){ if(n==0) return 1; return n*Fact(n-1); }
void solve()
{
    int a, b, c, cnt=0;
    cin>>a>>b>>c;
    if(a){
        a--, cnt++;
    }
    if(b){
        b--, cnt++;
    }
    if(c){
        c--, cnt++;
    }
    if(a<b) swap(a, b);
    if(a<c) swap(a, c);
    if(a && b){
        a--, b--, cnt++;
    }
    if(a && c){
        a--, c--, cnt++;
    }
    if(b && c) {
        b--, c--, cnt++;
    }
    if(a && b && c){
        a--, b--, c--, cnt++;
    }
    cout<<cnt<<endl;


}

int main()
{
    int t;
    cin>>t;
    while(t--)
    solve();

    return 0;
}