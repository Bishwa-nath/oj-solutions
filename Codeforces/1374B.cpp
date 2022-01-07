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
        lli n, a, b, x;
        cin>>n;
        a = b = 0;
        while(n%2LL==0)
        {
            n/=2;
            a++;
        }
        while(n%3LL==0){
            n/=3;
            b++;
        }
        if(n>1) cout<<-1<<endl;
        else if(a>b) cout<<-1<<endl;
        else{
            x = b - a;
            x += b;
            cout<< x <<endl;
        }
    }

    return 0;
}