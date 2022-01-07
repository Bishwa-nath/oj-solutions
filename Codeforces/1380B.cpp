#include <bits/stdc++.h>
using namespace std;

#define lli long long int
#define forn for(int i=0; i<n; i++)
#define form for(int i=0; i<m; i++)
#define forj for(int j=0; j<n; j++)
#define PI 3.141592653589793
#define MOD 1000000007
#define sorta sort(a, a+n)
#define nln cout<<endl

int main()
{
    int t;
    cin>>t;

    while(t--)
    {
        string str;
        int n, r=0, s=0, p=0;
        cin>>str;
        n = str.length();

        for(int i=0; i<n; i++)
        {
            if(str[i]=='R') r++;
            else if(str[i]=='S') s++;
            else p++;
        }

        if(r>=s && r>=p){
            while(n--) cout<<'P';
        }
        else if(p>=s && p>=r){
            while(n--){
                cout<<'S';
            }
        }
        else if(s>=r && s>=p){
            while(n--){
                cout<<'R';
            }
        }
        nln;
    }
    return 0;
}