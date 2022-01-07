#include <bits/stdc++.h>
using namespace std;

#define lli long long int
#define forn for(int i=0; i<n; i++)
#define form for(int i=0; i<m; i++)
#define forj for(int j=0; j<n; j++)
#define PI 3.141592653589793
#define MOD 1000000007
#define sorta sort(a, a+n)
#define mx max(a, b)
#define mn min(a, b)


void solve();

int main()
{
    int t;
    cin>>t;
    while(t--)
    solve();

    return 0;
}

void solve()
{
    int n, cnt=0,res=0;
    string s;
    cin>>n>>s;

    for(int i=0; i<n; i++)
    {
        if(s[i] == '(')
            cnt++;
        else{
            cnt--;
            if(cnt<0)
                res = max(res, 0 - cnt);
        }
    }

    cout<<res<<endl;
}