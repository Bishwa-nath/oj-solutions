#include <bits/stdc++.h>
using namespace std;

#define rapid()  ios_base::sync_with_stdio(false); cin.tie(NUll); cout.tie(NUll);
#define in()     freopen("input.txt","r",stdin);
#define out()    freopen("output.txt","w",stdout);
#define set_str  set<string> st
#define forin    for(int i=0; i<n; i++)
#define forim    for(int i=0; i<m; i++)
#define forjn    for(int j=0; j<n; j++)
#define forjm    for(int j=0; j<m; j++)
#define Pi       3.141592653589793
#define MOD      1000000007
#define nln      cout<<"\n"
#define nl       '\n'
#define eps      1e-9
#define d_point cout<<fixed<<setprecision

typedef long long   ll;
const int MAX_CHARS = 256;

bool is_palindrome(string s){ return equal(s.begin(), s.begin() + s.size()/2, s.rbegin()); }
bool is_prime(int n) {int root= sqrt(n); if(n==1) return false; for(int i=2; i<=root; i++){ if(n%i==0) return false;} return true; }
int digitsOfFact(int n) { double x=0; for(int i=1; i<=n; i++){ x+= log10(i);} int res = x + 1 + eps; return res; }
int lcm(ll a,ll b) { ll lar = max(a, b); ll small = min(a, b); for (ll i = lar; ; i += lar){if (i % small == 0) return i;} }
int gcd(int a,int b) { if (b == 0) return a; return gcd(b, a % b); }
int Fact(int n){ if(n==0) return 1; return n*Fact(n-1); }
ll digit_rev(ll n){ ll ret=0; while(n>0){ret *= 10;int temp = n%10;ret += temp;n/=10;}return ret;}
int distinct_subStr(string s, int len){ set_str; for(int i=0; i<len; i++) for(int j=1; j<=len-i; j++) st.insert(s.substr(i,j)); return st.size();}

int main()
{
    set<ll> num;
    num.insert(1);
    set<ll>::iterator it;
    it = num.begin();
    ll newnum;
    int count =0;
    while(++count < 11)
    {
        newnum = *it;
        num.insert(newnum*2);
        num.insert(newnum*3);
        num.insert(newnum*5);
        it++;
    }

    newnum = *it;
    cout<<"The 1500'th ugly number is "<<newnum<<"."<<endl;

    for(auto x: num)
        cout<<x<<endl;


    return 0;
}



