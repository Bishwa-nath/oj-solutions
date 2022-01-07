#include <bits/stdc++.h>
using namespace std;

#define lli long long int
#define vi vector<int>
#define forn for(int i=0; i<n; i++)
#define form for(int i=0; i<m; i++)
#define forj for(int j=0; j<n; j++)
#define sortn sort(a, a+n);
#define sortb sort(s.begin(), s.end())
#define reversen reverse(a, a+n)
#define reverseb reverse(s.begin(), s.end())
#define pi 2*acos(0.0)
#define MOD 1000000007
#define nln cout<<endl
#define eps 1e-9
#define nln cout<<endl
//boost::math::lcm (x, y);

bool is_prime(int n) {int root= sqrt(n); if(n==1) return false; for(int i=2; i<=root; i++){ if(n%i==0) return false;} return true; }
int gcd(int a, int b) {if (a == 0) return b; return gcd(b % a, a); }
int digitsOfFact(int n) { double x=0; for(int i=1; i<=n; i++){ x+= log10(i);} int res = x + 1 + eps; return res; }

int findGCD(vector<int> v, int n)
{
    int result = v[0];
    for (int i = 1; i <n; i++)
    {
        result = gcd(v[i], result);

        if(result == 1)
        {
            return 1;
        }
    }
    return result;
}

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        lli n, x, le=0, cnt=0;
        cin>>n>>x;
        int a[n];
        forn cin>>a[i];

        sort(a, a+n, greater<int>());

        for(int i=0; i<n; i++)
        {
            ++le;
            if((le*a[i])>=x){

                cnt++;
                le=0;
            }
        }


        cout<<cnt<<endl;
    }

    return 0;
}