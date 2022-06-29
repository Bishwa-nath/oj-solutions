#include <bits/stdc++.h>
using namespace std;

#define nl "\n"

int main()
{
    int r;
    cin>>r;
    if(r < 1200) cout << 1200 << nl;
    else if(r < 1400) cout << 1400 << nl;
    else if(r < 1600) cout << 1600 << nl;
    else if(r < 1900) cout << 1900 << nl;
    else if(r < 2100) cout << 2100 << nl;
    else if(r < 2300) cout << 2300 << nl;
    else if(r < 2400) cout << 2400 << nl;
    else if(r < 2600) cout << 2600 << nl;
    else cout << 3000 << nl;

    return 0;
}