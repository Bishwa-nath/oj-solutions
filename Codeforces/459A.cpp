#include <bits/stdc++.h>
using namespace std;
 
#define rapid() ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define in()    freopen("input.txt","r",stdin);
#define out()   freopen("output.txt","w",stdout);
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
 
int main()
{
    int x1, x2, y1, y2, x3, x4, y3, y4;
    cin>>x1>>y1>>x2>>y2;
    if(abs(x1-x2)==abs(y1-y2)){
        if((x1<x2 && y1<y2) || (x1>x2 && y1>y2))
            cout<<min(x1, x2)<<' '<<max(y1, y2)<<' '<<max(x1, x2)<<' '<<min(y1, y2)<<endl;
        else cout<<max(x1, x2)<<' '<<max(y1, y2)<<' '<<min(x1, x2)<<' '<<min(y1, y2)<<endl;
    }
    else if(x1==x2) {
        int a = abs(y1-y2);
        printf("%d %d %d %d\n", a+x1, y1, a+x1, y2);
    }
    else if(y1==y2){
        int a = abs(x1-x2);
        printf("%d %d %d %d", x1, a+y1, x2, a+y1);
    }
    else cout<<-1<<endl;
 
    return 0;
}