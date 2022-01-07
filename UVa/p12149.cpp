#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main()
{
    int n;
    cin >> n;
    while(true)
    {
        if(n == 0) break;

        ll G = 0;
        for(ll i=1; i<=n; i++)
            G += (i*i);

        cout << G << endl;
        cin >> n;
    }

    return 0;
}

