#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t, n;
    cin >> t;
    int x = 1;
    while(t--){
        int n, k, p, res = 0;
        cin >> n >> k >> p;
        res = (k+p)%n;
        if(res == 0)
        printf("Case %d: %d\n", x, n);
        else
        printf("Case %d: %d\n", x, res);
        x++;
    }


    return 0;
}

