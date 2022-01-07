#include <bits/stdc++.h>
using namespace std;

#define lli long long int
#define forn for(int i=0; i<n; i++)
#define form for(int i=0; i<m; i++)
#define forj for(int j=0; j<n; j++)
#define PI 3.141592653589793
#define MOD 1000000007
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
    int n, i = 2;
    lli a, res=1;
    string s = "";
    cin>>n>>a;

    while(a>0)
    {
        int t = a%10;
        if(t==2) s += "2";
        else if(t==3) s += "3";
        else if(t==4) s += "322";
        else if(t==5) s += "5";
        else if(t==6) s += "53";
        else if(t==7) s += "7";
        else if(t==8) s += "7222";
        else if(t==9) s += "7332";
        a/=10;
    }
    sort(s.begin(), s.end(), greater<char>());
    cout<<s<<endl;


}

int main()
{
    int t;
    //cin>>t;
    //while(t--)
    solve();

    return 0;
}