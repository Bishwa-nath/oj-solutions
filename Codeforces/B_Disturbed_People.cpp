#include <bits/stdc++.h>
using namespace std;

typedef long long   ll;

#define rapid()     ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define in()        freopen("input.txt","r",stdin);
#define out()       freopen("output.txt","w",stdout);
#define forin       for(int i=0; i<n; i++)
#define forim       for(int i=0; i<m; i++)
#define forjn       for(int j=0; j<n; j++)
#define forjm       for(int j=0; j<m; j++)
#define Pi          acos(-1)
#define MOD         1000000007
#define nln         cout<<"\n"
#define nl          "\n"
#define eps         1e-9
#define fraction(x)  cout<<setprecision(10)<< fixed << x << nl;
#define yesno       if(ok) cout << "YES" << endl; else cout << "NO" << endl;
 
bool is_palindrome(string s){ return equal(s.begin(), s.begin() + s.size()/2, s.rbegin()); }
bool is_prime(ll n) {ll root= sqrt(n); if(n==1) return false; for(ll i=2; i<=root; i++){ if(n%i==0) return false;} return true; }
void printv(const vector<int> &vec){ for(auto au: vec) cout << au << ' '; nln;}
void prints(const set<int> &st){ for(auto au: st) cout << au << ' '; nln; }
int digitsOfFact(int n) { double x=0; for(int i=1; i<=n; i++){ x+= log10(i);} int res = x + 1 + eps; return res; }
int gcd(int a,int b) { return __gcd(a, b) ; }
int lcm(int a, int b) { return (a*b)/__gcd(a, b); }
ll digit_rev(ll n){ ll ret=0; while(n>0){ret *= 10; int temp = n%10; ret += temp; n/=10;} return ret;}
int distinct_subStr(string s, int len){ set<string> st; for(int i=0; i<len; i++) for(int j=1; j<=len-i; j++) st.insert(s.substr(i,j)); return st.size();}

int main()
{
    //rapid();
    int n;
    cin>>n;
    int ar[n];
    forin cin>>ar[i];
    int ans = 0;
    for(int i=1; i<n-1; i++){
        if(ar[i] == 0 and ar[i-1] == 1 and ar[i+1] == 1){
            ans++;
            ar[i+1] = 0;
        }
    }
    cout << ans << nl;
    
    return 0;
}