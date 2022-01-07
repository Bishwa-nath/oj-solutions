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

int lcm(LL a,LL b)
{
    LL lar = max(a, b);
    LL small = min(a, b);
    for (LL i = lar; ; i += lar)
    {
        if (i % small == 0)
            return i;
    }
}

int gcd(LL a,LL b)
{
    if (b == 0)
        return a;
    return gcd(b, a % b);

}

lli fact(int n)
{
    if(n==1)
        return 1;
    return n*fact(n-1);
}

bool cmp(int a, int b)
{
    return a>b;
}


int main()
{
    int n;
    cin>>n;
    int a[n+1];
    int x;
    vector<int> v1, v2, v3;
   for(int i=1; i<=n; i++)
    {
        cin>>a[i];
        if(a[i]==1) v1.push_back(i);
        if(a[i]==2) v2.push_back(i);
        if(a[i]==3) v3.push_back(i);

    }

    int mn = min(v1.size(), min(v2.size(), v3.size()));

    if(mn==0) cout<<0<<endl;
    else{
        cout<<mn<<endl;
        for(int i=0; i<mn; i++)
        cout<<v1[i]<<" "<<v2[i]<<" "<<v3[i]<<endl;

    }

    return 0;
}