#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t, n;
    cin >> t;
    int k = 1;
    while(t--){

        cin >> n;
        int ar[n];
        sort(ar, ar+n);
        for(int i=0; i<n; i++)
            cin >> ar[i];

        printf("Case %d: %d\n", k, ar[n/2]);
        k++;
    }


    return 0;
}
