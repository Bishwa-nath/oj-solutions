#include <bits/stdc++.h>
using namespace std;

#define lli long long int
#define vi vector<int>
#define forn for(int i=0; i<n; i++)
#define form for(int j=0; j<m; j++)
#define forj for(int j=0; j<n; j++)
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

        if(n%2 == 0)
        {
            int x = n/2;
            cout<<x<<" "<<x<<endl;
        }

        else
        {
            int j=1;
            for(int i=2; i*i<=n; i++){
                if(n%i==0){
                    j = i;
                    break;
                }
            }
            if(j==1)
            cout<<1<<" "<<(n-1)<<endl;
            else{
                int x = n/j;
                cout<<x<<" "<<(n-x)<<endl;
            }
        }

    }
    return 0;

}