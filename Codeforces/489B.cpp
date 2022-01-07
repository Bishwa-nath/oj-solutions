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

int gcd(int a, int b)
{
    if (a == 0)
        return b;
    return gcd(b % a, a);
}

int factDigits(int n)
{
    double x=0;
    for(int i=1; i<=n; i++)
    {
        x+= log10(i);
    }
    int res = x + 1 + eps;
    return res;
}
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
    int n, m, cnt=0;
    cin>>n;
    int a[n];
    forn cin>>a[i];
    cin>>m;
    int b[m];
    form cin>>b[i];

    sort(a, a+n);
    sort(b, b+m);

    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            if(abs(a[i] - b[j])<=1 &&b[j] != -1){
                cnt++;
                b[j] = -1;
                break;
            }
        }
    }

    cout<<cnt<<endl;

    return 0;
}