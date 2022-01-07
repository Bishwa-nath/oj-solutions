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
//#define mn min(a, b)
#define nln cout<<endl

const int N = 51;
int a[N][N];

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n, m;
        set<int> r, c;
        r.clear();
        c.clear();

        cin>>n>>m;
        //int a[n][m];

        for(int i=1; i<=n; i++)
        {
            for(int j=1; j<=m; j++)
            {
                cin>>a[i][j];
                if(a[i][j] == 1)
                    r.insert(i), c.insert(j);
            }
        }
        int mn = min(n - r.size(), m - c.size());

        if(mn%2) cout<<"Ashish\n";
        else cout<<"Vivek\n";
    }

    return 0;
}