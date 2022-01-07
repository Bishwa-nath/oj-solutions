#include <bits/stdc++.h>
using namespace std;

#define lli long long int
#define forn for(int i=0; i<n; i++)
#define form for(int i=0; i<m; i++)
#define forj for(int j=0; j<n; j++)
#define PI 3.141592653589793
#define MOD 1000000007
#define sorta sort(a, a+n)

bool isPrime(lli x)
{
    if(x==1) return 0;
    int root, okPrime=0;
    root = sqrt(x);
    for(int i=2; i<=root; i++)
    {
        if(x%i==0)
        {
            okPrime=1;
            break;
        }
    }
    if(okPrime==0)
        return 1;
    else return 0;
}

int main()
{
    int n;
    cin>>n;
    lli x;
    int a[n];
    for(int i=0; i<n; i++)
    {
        cin>>x;
        lli root = sqrt(x);
        if(root*root == x){
            if(isPrime(root))
                cout<<"YES"<<endl;
            else cout<<"NO"<<endl;
        }
        else cout<<"NO"<<endl;
    }


    return 0;
}