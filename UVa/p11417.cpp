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

        int G = 0;
        for(int i=1; i<n; i++)
            for (int j=i+1; j<=n; j++)
                G += __gcd(i, j);

        cout << G << endl;
        cin >> n;
    }

    return 0;
}
